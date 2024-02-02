import pymongo

CLIENT = pymongo.MongoClient("mongodb://localhost:27017")
DB = CLIENT["database"]
COLLECTION = DB["links"]



def insert_url_info(hash:str, url:str):
    link_dict = {"hash": hash, "url": url}
    res = COLLECTION.insert_one(link_dict)
    return res

def seek_url(hash: str):
    res = COLLECTION.find_one({"hash": hash})
    return res
