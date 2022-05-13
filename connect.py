from gc import collect
from matplotlib import collections
from pymongo import MongoClient
mongo_db = MongoClient("mongodb://localhost:27017")
db = mongo_db['test']
collection = db['test']
collection.insert_one({"name": "test"})