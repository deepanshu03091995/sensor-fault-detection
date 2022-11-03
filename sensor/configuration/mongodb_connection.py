import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
from dotenv import load_dotenv

load_dotenv()
import certifi
import os


ca = certifi.where()


class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME):
        try:
            if MongoDBClient.client is None:
                # mongo_db_url = os.getenv(MONGODB_URL_KEY)
                mongo_db_url = "mongodb+srv://Deepadmin:Root@cluster0.mhel9.mongodb.net/admin?authSource=admin&replicaSet=atlas-6qsgpk-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
                if mongo_db_url is None:
                    raise Exception(f"Environment Key :{MONGODB_URL_KEY} id not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client["database_name"]
            self.database_name = database_name
        except Exception as e:
            raise e
