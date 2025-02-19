import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)

# NOTE: these are currently placeholders - need to implement database
# and PyMongo in order to make use of these
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

# currently for local developement only
CORS(app, origins=["http://localhost:5173"])

@app.route("/test", methods=["GET"])
def get_events():
    return {"message": "CORS works!"}