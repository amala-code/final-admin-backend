from utils.db import db, members_collection

# Check current counter value
current_counter = db.counters.find_one({"_id": "memberid"})
print(f"Current counter: {current_counter}")

# Find max ID in members collection
max_id = 0
for doc in members_collection.find({}, {"id": 1}):
    id_val = doc.get("id")
    if id_val and isinstance(id_val, str) and id_val.isdigit():
        n = int(id_val)
        if n > max_id:
            max_id = n

print(f"Max ID in members collection: {max_id}")

# Reset counter
db.counters.delete_one({"_id": "memberid"})
print("Counter deleted")

# Set new counter value
db.counters.insert_one({"_id": "memberid", "seq": max_id})
print(f"Counter reset to: {max_id}")