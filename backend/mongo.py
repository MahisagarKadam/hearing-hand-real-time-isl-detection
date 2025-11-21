from urllib.parse import quote_plus
from pymongo import MongoClient
from pymongo.errors import PyMongoError

# MongoDB local connection string
client = MongoClient("mongodb://localhost:27017/")  # Local MongoDB connection string

# Connecting to the "login_info" database and "login0" collection
db = client["login_info"]
col = db["login0"]

# Validate email and password
def validate(email, password):
    if email and password:
        try:
            data = col.find_one({"email": email, "password": password})
            return True if data else False
        except PyMongoError as e:
            print(f"Error during validation: {e}")
            return False
    else:
        return False

# Insert data into database
def insert(name, email, password, disability, role, dob, slink, glink, llink, bio, gender):
    if name and check(email) and password and disability and role:
        query = {
            "name": name,
            "email": email,
            "password": password,
            "disability": disability,
            "role": role,
            "dob": dob,
            "slink": slink,
            "glink": glink,
            "llink": llink,
            "bio": bio,
            "gender": gender
        }
        try:
            col.insert_one(query)
            return True
        except PyMongoError as e:
            print(f"Error during insert: {e}")
            return False
    else:
        return False

# Update data in database
def update(name, email, disability, role, dob, slink, llink, glink, bio, gender):
    if not check(email):  # Check if email already exists in DB
        if name and email:
            try:
                col.update_many({"email": email}, {"$set": {
                    "name": name,
                    "disability": disability,
                    "role": role,
                    "dob": dob,
                    "slink": slink,
                    "glink": glink,
                    "llink": llink,
                    "bio": bio,
                    "gender": gender
                }})
                return True
            except PyMongoError as e:
                print(f"Error during update: {e}")
                return False
        else:
            return False
    else:
        return False

# Update password
def updatepwd(email, password):
    if not check(email):  # Check if email exists in DB
        if password and email:
            try:
                col.update_many({"email": email}, {"$set": {"password": password}})
                return True
            except PyMongoError as e:
                print(f"Error during password update: {e}")
                return False
        else:
            return False
    else:
        return False

# Check if email already exists
def check(email):
    if email:
        try:
            data = col.find_one({"email": email})
            return False if data else True  # False if email exists, True if it doesn't
        except PyMongoError as e:
            print(f"Error during check: {e}")
            return False
    else:
        return False

# Show data from database
def show(email):
    if email:
        try:
            data = col.find_one({"email": email}, {"_id": 0})  # Exclude _id field
            return data if data else None
        except PyMongoError as e:
            print(f"Error during show: {e}")
            return None
    else:
        return None
