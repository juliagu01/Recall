from Recall.backend.client import client

db = client["recall"]
days = db["days"]

def add_day(date, happening_ids):
  days.insert_one({
    "date": date,
    "happening_ids": happening_ids
  })
