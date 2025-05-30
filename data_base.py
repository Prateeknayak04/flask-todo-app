
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGO_URI")
if not uri:
    raise ValueError("MONGODB_URI environment variable is not set")
client = MongoClient(uri)
db = client["tododb"]
todos_collection = db["todos"]


def get_all_todos():
    return list(todos_collection.find({}))

def add_todo(task):
    return todos_collection.insert_one({
        "task": task,
        "done": False
    })

def toggle_done(todo_id, done):
    return todos_collection.update_one(
        {"_id": todo_id},
        {"$set": {"done": done}}
    )

def delete_todo(todo_id):
    return todos_collection.delete_one({"_id": todo_id})

def update_todo(todo_id, new_task):
    return todos_collection.update_one(
        {"_id": todo_id},
        {"$set": {"task": new_task}}
    )
