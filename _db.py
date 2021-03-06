from tracemalloc import begin
import pymongo
import os
import time
from dotenv import load_dotenv



load_dotenv()

client = pymongo.MongoClient(os.getenv("LOCAL_URI"))

db = client.users
post = {"_id":0,
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": time.strftime("%c"),
        "email": "555@gmail.com"}
        
posts = db.posts
start = time.time()
post_id = posts.insert_one(post).inserted_id

###############################################################################
### GET
###

def get_data_from_email(email):
    return posts.find_one({'email': email})

###############################################################################
### ADD
###

def add_post(post):
    post_id = posts.insert_one(post).inserted_id
    return post_id

###############################################################################
### SET
###

def set_email(email):
    posts.update_one({"email": email}, {"$set": {"email": email}})

def set_password(email, password):
    posts.update_one({"email": email}, {"$set": {"password": password}})

def set_name(email, name):
    posts.update_one({"email": email}, {"$set": {"name": name}})

def set_author(email, author):
    posts.update_one({"email": email}, {"$set": {"author": author}})

# print(db)
print(get_data_from_email("555@gmail.com")['author'])
print(post["_id"])
set_author("555@gmail.com", "Alice")
print(get_data_from_email("555@gmail.com")['author'])
posts.delete_many({})
stop = time.time()

print(stop - start) # Local Server is 12-60 times faster than cloud server

