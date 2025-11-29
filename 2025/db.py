import os
from datetime import datetime
from functools import wraps
from typing import TypedDict

from pymongo import MongoClient
from pymongo.server_api import ServerApi

MONGODB_URI = os.getenv("MONGODB_URI")


def init_client():
    return MongoClient(
        MONGODB_URI,
        server_api=ServerApi(version="1", strict=True, deprecation_errors=True),
    )


client = init_client()
try:
    # Send a ping to confirm a successful connection
    client.admin.command({"ping": 1})
    print("Pinged your deployment. You successfully connected to MongoDB!")
finally:
    client.close()


def create_record(day, result_time, timestamp, comment, person, code):
    client = init_client()
    try:
        collection = client.aoc.records
        record = Record(
            day=day,
            result_time=result_time,
            timestamp=timestamp,
            person=person,
            code=code,
        )
        inserted = collection.insert_one(record)
        return inserted.inserted_id
    finally:
        client.close()


class Record(TypedDict):
    day: int
    result_time: float
    timestamp: datetime
    person: str
    comment: str
    code: str
