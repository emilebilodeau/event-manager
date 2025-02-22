import os
import json
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.errors import PyMongoError

load_dotenv()

app = Flask(__name__)

# currently for local developement only
CORS(app, origins=["http://localhost:5173"])

app.config["MONGO_URI"] = os.getenv("MONGO_URI")

client = MongoClient(app.config["MONGO_URI"])
database = client.get_database("event_manager")

@app.route("/events/create", methods=["POST"])
def create_event():
    """ Creates a new event """
    try:
        event_manager_db = database.get_collection("events")
        
        data = request.get_json()

        query = {
            "name" : data.get("name"), 
            "description" : data.get("description"),
            "date" : data.get("date"),
            "location" : data.get("location")
        }
        res = event_manager_db.insert_one(query)

        if res.inserted_id:
            return jsonify({"message": "Event created successfully!", "id": str(res.inserted_id)}), 201
        return jsonify({"error": "Failed to create event"}), 500

    except PyMongoError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.route("/events/test", methods=["GET"])
def get_mongo_events():
    """ Test endpoint """
    try:
        database = client.get_database("test_db")
        test = database.get_collection("test_col")

        query = {"test" : "test_value"}
        res = test.find_one(query)
        
        if res:
            # "_id" is of object type ObjectId which is not JSON serializable
            res["_id"] = str(res["_id"])
            return jsonify(res)
        else:
            jsonify({"error": "Document not found"}), 200

    except Exception as e:
        print(f"Unable to find the document due to the following error: {str(e)}")
