from config.db_config import DATABASE

import sqlalchemy as sql
from sqlalchemy.types import Integer, String, Float, DateTime, Boolean
from sqlalchemy import Table, MetaData, Column, text
from sqlalchemy import Identity, func, select


class Car:

    def __init__(self):
        self.database = DATABASE()
        self.engine = self.database.get_database()
        self.name = "cars_table"
        self.meta = MetaData()

    def create_table(self):
        with self.database.get_connection() as conn:
            # cursor
            cursor = conn.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS {} \
            (   name VARCHAR(255) NOT NULL, \
                price integer NOT NULL, \
                abtest VARCHAR(255) NOT NULL, \
                vehicleType VARCHAR(255), \
                yearOfRegistration VARCHAR(4) NOT NULL, \
                gearbox VARCHAR(255), \
                powerPS integer NOT NULL, \
                model VARCHAR(255), \
                kilometer integer, \
                monthOfRegistration VARCHAR(255) NOT NULL, \
                fuelType VARCHAR(255), \
                brand VARCHAR(255) NOT NULL, \
                notRepairedDamage VARCHAR(255), \
                dateCreated DATE NOT NULL, \
                postalCode VARCHAR(255) NOT NULL);".format(
                    self.name
                )
            )

    def write_postgresql(self, df):

        cars_seq = [tuple(x) for x in df.collect()]

        records_list_template = ",".join(["%s"] * len(cars_seq))

        insert_query = "INSERT INTO cars_table (name, price, abtest, vehicleType, yearOfRegistration, gearbox, powerPS, \
                            model, kilometer, monthOfRegistration, fuelType, brand, notRepairedDamage, dateCreated, postalCode \
                            ) VALUES {}".format(
            records_list_template
        )

        with self.database.get_connection() as conn:
            # cursor
            cursor = conn.cursor()
            cursor.execute(insert_query, cars_seq)

    def get_insterted_data(self):

        with self.database.get_connection() as conn:
            # cursor
            cursor = conn.cursor()

            postgreSQL_select_Query = "select brand, model, price from cars_table"

            cursor.execute(postgreSQL_select_Query)

            cars_records = cursor.fetchmany(2)

            print("Printing 2 rows")
            for row in cars_records:
                print(
                    "Brand = ",
                    row[0],
                )
                print("Model = ", row[1])
                print("Price  = ", row[2], "\n")
