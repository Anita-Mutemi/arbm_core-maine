from pymongo import MongoClient # type: ignore
from dotenv import dotenv_values # type: ignore

__all__ = ["MongoDb"]

config = dotenv_values(".env")


_mongodb_client = MongoClient(config["MONGO_URI"], uuidRepresentation="standard")
MongoDb = _mongodb_client[config["MONGO_DB_NAME"]]