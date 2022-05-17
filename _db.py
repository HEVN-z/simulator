import pymongo
import os
import time
from dotenv import load_dotenv
load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = client.users
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": time.strftime("%c")}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
posts.delete_many({})



print(db)