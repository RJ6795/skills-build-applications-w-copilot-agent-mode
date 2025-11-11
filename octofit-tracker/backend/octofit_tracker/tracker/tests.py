from django.test import TestCase
from django.conf import settings
from pymongo import MongoClient

class PopulateAndReadDBTest(TestCase):
    """Quick integration-style test that reads inserted test documents with pymongo.
    Note: This test requires a running MongoDB on localhost:27017 and the
    `populate_db.py` script to have been run. It's included for convenience.
    """
    def test_read_populated_docs(self):
        client = MongoClient("mongodb://localhost:27017")
        db = client['octofit_db']
        col = db['activities']
        count = col.count_documents({"source": "populate_script"})
        self.assertGreaterEqual(count, 1)
        client.close()
