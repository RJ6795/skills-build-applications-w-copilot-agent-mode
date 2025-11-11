"""
Populate the octofit_db database with test data

This script uses pymongo to connect to localhost:27017 and insert sample activity
documents into the `activities` collection of the `octofit_db` database.
"""
from pymongo import MongoClient
from datetime import datetime, timedelta

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "octofit_db"
COLLECTION = "activities"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
col = db[COLLECTION]

# Clear existing test documents inserted by this script (optional and safe for local test DB)
col.delete_many({"source": "populate_script"})

base_time = datetime.utcnow()

sample_docs = [
    {
        "user": "alice",
        "activity_type": "running",
        "duration_minutes": 30,
        "calories": 300,
        "timestamp": base_time - timedelta(days=1),
        "source": "populate_script",
    },
    {
        "user": "bob",
        "activity_type": "cycling",
        "duration_minutes": 45,
        "calories": 450,
        "timestamp": base_time - timedelta(hours=5),
        "source": "populate_script",
    },
    {
        "user": "alice",
        "activity_type": "yoga",
        "duration_minutes": 60,
        "calories": 200,
        "timestamp": base_time - timedelta(days=2),
        "source": "populate_script",
    },
]

result = col.insert_many(sample_docs)
print(f"Inserted {len(result.inserted_ids)} documents into {DB_NAME}.{COLLECTION}")
client.close()
