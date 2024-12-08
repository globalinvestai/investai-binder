from pyspark.sql.types import (
    StructField,
    StructType,
)
from pyspark.sql.types import (
    StructField,
    StructType,
    StringType,
    LongType,
    TimestampType,
    ShortType,
    DateType,
)
from enum import Enum
import json
import os
import inspect


class DATATYPE(Enum):
    STRING = StringType
    TIMESTAMP = TimestampType
    LONG = LongType
    SHORT = ShortType
    DATE = DateType

    def get_data_type(type):
        try:
            return DATATYPE[type].value
        except KeyError:
            return None


class Schema:
    """Utility class"""

    def __init__(self, filename):
        # Open and read the JSON file

        dir = __file__.replace("schema.py", "")
        print(dir, __file__)
        with open(dir + filename + ".json", "r") as file:
            data = json.load(file)

        # Print the data
        # print(data)
        self.structType = data.get("columns")

    def create_schema(self):
        struct = lambda x, y, nullable: StructField(
            x, DATATYPE.get_data_type(y)(), nullable
        )

        return StructType(
            [
                struct(s.get("column_name"), s.get("data_type"), s.get("nullable"))
                for s in self.structType
            ]
        )
