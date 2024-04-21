from Recall.backend.client import client
from Recall.Recall import app

db = client["recall"]
happenings = db["happenings"]

@app.route("/happenings/", methods=["POST"])
def add_happening():
    raw_happening = request.get_json()
    name = raw_happening["name"]
    notes = raw_happening["notes"]
    happenings.insert_one({
        "name": name,
        "notes": notes,
    })

@app.route("/happenings/", methods=["PUT"])
def edit_happening_notes():
    raw_happening = request.get_json()
    id = raw_happening["_id"]
    notes = raw_happening["notes"]
    happenings.find_one_and_update(
        {"_id": id}, 
        {"$set": {"notes": notes}},
    )

@app.route("/days/", methods=["GET"])
def get_happening():
    raw_happening = request.get_json()
    id = raw_happening["_id"]
    happening = happenings.find_one({"_id": id})
    return happening.to_json()
