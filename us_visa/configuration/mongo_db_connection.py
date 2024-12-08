import sys
import os
import certifi
from pymongo import MongoClient
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY

class MongoDBClient:
    """
    Class Name :   MongoDBClient
    Description :   This class initializes a MongoDB client and connects to a specified database.
    
    Output      :   MongoDB database connection object
    On Failure  :   Raises USvisaException
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if not mongo_db_url:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = MongoClient(mongo_db_url, tlsCAFile=certifi.where())
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info(f"MongoDB connection to '{database_name}' successful")
        except Exception as e:
            logging.error("Failed to connect to MongoDB")
            raise USvisaException(e, sys)
