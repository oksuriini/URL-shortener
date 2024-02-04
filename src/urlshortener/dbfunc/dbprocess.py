from socket import error
import pymongo


def insert_url_info(hash: str, url: str):
    res = ""
    try:
        CLIENT = pymongo.MongoClient("mongodb://localhost:27017")
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
