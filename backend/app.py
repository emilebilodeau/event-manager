import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

# currently for local developement only
CORS(app, origins=["http://localhost:5173"])

app.config["MONGO_URI"] = os.getenv("MONGO_URI")

client = MongoClient(app.config["MONGO_URI"])

@app.route("/events/test", methods=["GET"])
def get_mongo_events():
    try:
        database = client.get_database("test_db")
        test = database.get_collection("test_col")

        query = {"test" : "test_value"}
        res = test.find_one(query)
        
        if res:
            # "_id" is of object type ObjectId which is not JSON serializable
            res["_id"] = str(res["_id"])
            return jsonify(res), 200
        return {}

    except Exception as e:
        print(f"Unable to find the document due to the following error: {str(e)}")
