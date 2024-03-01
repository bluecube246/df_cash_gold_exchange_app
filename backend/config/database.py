from pymongo import MongoClient
from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
mongo_id = os.environ.get("MONGODB_ID")
password = os.environ.get("MONGODB_PWD")

client = MongoClient(f"mongodb+srv://{mongo_id}:{password}@cubecluster.bhdqotz.mongodb.net/?retryWrites=true&w=majority")

df_db = client['dnf']

db = client.TodoList
collection_name = db["todo_collection"]