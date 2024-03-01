from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name, df_db
from schema.schemas import list_serial, list_serial_2
from bson import ObjectId
from api.constants import average_auction_dict

router = APIRouter()


# GET Request Method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


@router.get("/api/average")
async def get_todos():
    results = []
    for item, collection in average_auction_dict.items():
        result = df_db[collection].find().sort({"$natural": 1}).limit(1)
        results.extend(list_serial_2(result))

    return {
        "data": results
    }


# POST REQUEST Method
@router.post("/")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))


# PUT Request Method
@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})


# Delete Request Method
@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})