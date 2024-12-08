from config.spark_config import Spark
from pyspark.sql.types import (
    StructField,
    StructType,
    StringType,
    LongType,
    TimestampType,
    ShortType,
    DateType,
)
from pyspark.sql.functions import col
from db.cars import Car


def clean_drop_data(df):

    df_dropped = df.drop("dateCrawled", "nrOfPictures", "lastSeen")
    df_filtered = df_dropped.where(col("seller") != "gewerblich")
    df_dropped_seller = df_filtered.drop("seller")
    df_filtered2 = df_dropped_seller.where(col("offerType") != "Gesuch")
    df_final = df_filtered2.drop("offerType")

    return df_final


spark = Spark()


df = spark.loadDFWithSchema("autos.csv", "car_table")
print(df.show())

df = clean_drop_data(df)

df.show(1, vertical=True)
car = Car()
car.create_table()
car.write_postgresql(df)
car.get_insterted_data()
