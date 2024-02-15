import os
from socket import error
import pymongo

CONNECTION_NAME = os.getenv("MONGODB_URL")
if os.getenv("MONGODB_PORT"):
    CONNECTION_PORT = os.getenv("MONGODB_PORT")
else:
    print("MongoDB port not provided defaulting to 27017")
    CONNECTION_PORT = "27017"


def insert_url_info(hash: str, url: str):
    res = ""
    try:
        CLIENT = pymongo.MongoClient(f"mongodb://{CONNECTION_NAME}:{CONNECTION_PORT}")
        DB = CLIENT["database"]
        COLLECTION = DB["links"]
        link_dict = {"hash": hash, "url": url}
        res = COLLECTION.insert_one(link_dict)
    except error:
        res = "Error with establishing connectino to MongoDB"

    return res


def seek_url(hash: str):
    res = ""
    try:
        CLIENT = pymongo.MongoClient("mongodb://localhost:27017")
        DB = CLIENT["database"]
        COLLECTION = DB["links"]
        res = COLLECTION.find_one({"hash": hash})
    except error:
        res = "Error with establishing connectino to MongoDB"

    return res
