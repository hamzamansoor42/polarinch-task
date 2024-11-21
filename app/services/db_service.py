from pymongo import MongoClient
import os

client = MongoClient("mongodb://root:password@localhost:27017")
db = client["receipt_app"]
receipts_collection = db["receipts"]

def save_receipt_data(data):
    """Save parsed receipt data to MongoDB."""
    receipts_collection.insert_one(data)

def fetch_analytics():
    """Fetch analytics from MongoDB."""
    pipeline = [
        {"$unwind": "$items"},
        {
            "$group": {
                "_id": "$date",
                "total_spent": {"$sum": "$items.price"},
                "items_count": {"$sum": 1},
            }
        },
        {"$sort": {"_id": 1}}
    ]
    return list(receipts_collection.aggregate(pipeline))
