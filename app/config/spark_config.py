from pyspark.sql import SparkSession
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
from pyspark.sql.functions import col
from pyspark.sql.types import (
    StructField,
    StructType,
)
from schema.schema import Schema


class Spark:
    """Spark Utility Class"""

    def __init__(self):

        self.spark = SparkSession.builder.getOrCreate()

    def loadDFWithoutSchema(self, filename):
        df = self.spark.read.format("csv").option("header", "true").load(filename)

        return df

    def loadDFWithSchema(self, filename, table_name):

        schema = Schema(table_name).create_schema()
        print(schema)

        df = (
            self.spark.read.format("csv")
            .schema(schema)
            .option("header", "true")
            .load(filename)
        )

        return df

    def loadDF(self, data, schema):
        """Load Data Frame from a list of tuple data and schema"""
        df = self.spark.createDataFrame(data, schema=schema)

        return df

    def loadPandasDF(self, data, schema):
        """Load Data Frame from a dictionary data and schema"""
        df = self.spark.createDataFrame(data)

        return df
