
import pandas as pd
from pymongo import MongoClient
mongo_client = MongoClient("mongodb+srv://ssharma:saritapassword@b2b-backbone-test.3wiap.mongodb.net/")
mongo_db = mongo_client.get_database("eu_b2b")

collection = mongo_db.consumption_de_p_kwh_custom # collection name

collection.delete_many({})