from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv, find_dotenv
from routes.route import router
import os

load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)
