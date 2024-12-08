from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import psycopg2


class DATABASE:
    def __init__(self):
        load_dotenv()
        self.user = os.getenv("DB_USERNAME")
        self.password = os.getenv("DB_PASSWORD")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.database = os.getenv("DB_DATABASE")

        self.POSTGRES_DBCONN = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        self.engine = create_engine(self.POSTGRES_DBCONN, pool_pre_ping=True)

    def get_database(self):
        return self.engine

    def get_connection(self):
        conn = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )

        if conn:
            print("Connect to Postgres")
        else:
            print("Failed Connect to Postgres")

        return conn
