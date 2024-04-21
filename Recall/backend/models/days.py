from Recall.backend.client import client
from Recall.Recall import app

db = client["recall"]
days = db["days"]

@app.route("/days/", methods=["POST"])
def add_day():
    raw_day = request.get_json()
    date = raw_day["date"]
    happening_ids = raw_day["happening_ids"]
    days.insert_one({
        "date": date,
        "happening_ids": happening_ids,
    })

@app.route("/days/", methods=["GET"])
def get_day():
    raw_day = request.get_json()
    date = raw_day["date"]
    day = days.find_one({"date": date})
    return day.to_json()
