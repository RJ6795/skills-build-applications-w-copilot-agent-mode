"""Verify test data exists in octofit_db.activities using pymongo."""
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "octofit_db"
COLLECTION = "activities"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
col = db[COLLECTION]

count = col.count_documents({"source": "populate_script"})
print(f"Found {count} test documents in {DB_NAME}.{COLLECTION}")
for doc in col.find({"source": "populate_script"}):
    print(doc)
client.close()
