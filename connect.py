import pymongo
import time

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test

print(db)
db = client['test']
collection = db['test']
history = collection['history']
history.insert_one({"_id":1,"name": "5555"})
# start = time.time()
# y = collection.find({"name": "5555"})
# print('cursor object',y.cursor_id)
# print(y)
# end = time.time()
# print(end-start)
