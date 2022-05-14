import pymongo
import time

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test

print(db)
db = client['test']
collection = db['test']
history = collection['history']
# history.insert_one({"_id":1,"name": "Alice"})
history.update_one({"_id":1},{"$set":{"no": "126354"}})
history.update_one({"_id":1},{"$set":{"name": "Alice"}})
# start = time.time()
y = history.find_one({"_id": 1})
name = y['name']
no = y['no']
# print('cursor object',y.cursor_id)
print(name)
print(no)
# end = time.time()
# print(end-start)
