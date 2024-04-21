from Recall.backend.client import client
from Recall.Recall import app

db = client["recall"]
happening_formats = db["happening_formats"]

@app.route("/happening-formats/", methods=["POST"])
def add_format():
    raw_format = request.get_json()
    name = raw_format["name"]
    labels = raw_format["labels"]
    happening_formats.insert_one({
        "name": name,
        "labels": labels,
    })

@app.route("/happening-formats/", methods=["PUT"])
def edit_format():
    raw_format = request.get_json()
    id = raw_format["_id"]
    name = raw_format["name"]
    notes = raw_format["notes"]
    happening_formats.find_one_and_update(
        {"_id": id}, 
        {"$set": {"name": name, "notes": notes}},
    )

@app.route("/happening-formats/", methods=["GET"])
def get_formats():
    formats = list(happening_formats.find({}))
    return formats.to_json()
