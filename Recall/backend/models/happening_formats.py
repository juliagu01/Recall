from Recall.backend.client import client

db = client["recall"]
happening_formats = db["happening_formats"]

def add_format(name, labels_str):
  labels = labels_str.split("|")
  happening_formats.insert_one({
    "name": name,
    "labels": labels
  })

def edit_format_labels(id, labels_str):
  labels = labels_str.split("|")
  happening_formats.find_one_and_update(
    {"_id": id}, 
    {"$set": {"labels": labels}}
  )
