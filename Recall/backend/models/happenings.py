from Recall.backend.client import client

db = client["recall"]
happenings = db["happenings"]

def add_happening(name, notes):
  happenings.insert_one({
    "name": name,
    "notes": notes
  })

def edit_happening_notes(id, notes):
  happening_formats.find_one_and_update(
    {"_id": id}, 
    {"$set": {"notes": notes}}
  )
