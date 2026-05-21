import os
import json
from datetime import datetime

BASE_DIR = os.path.expanduser("~/Company")
EMPLOYEE_DB = os.path.join(BASE_DIR, "employees.json")

os.makedirs(BASE_DIR, exist_ok=True)

if not os.path.exists(EMPLOYEE_DB):
    with open(EMPLOYEE_DB, "w") as f:
        json.dump({}, f)

def load_db():
    with open(EMPLOYEE_DB, "r") as f:
        return json.load(f)

def save_db(data):
    with open(EMPLOYEE_DB, "w") as f:
        json.dump(data, f, indent=4)

def generate_password(length=12):

    import random
    import string

    chars = string.ascii_letters + string.digits + "!@#$%"

    return ''.join(random.choice(chars) for _ in range(length))


def reset_password():
    import random
    import string

    username = input("Enter username: ")
    db = load_db()

    if username not in db:
        print("User not found.")
        return

    chars = string.ascii_letters + string.digits + "!@#$%"
    new_password = ''.join(random.choice(chars) for _ in range(12))

    db[username]["password"] = new_password
    db[username]["password_reset_date"] = str(datetime.now())

    save_db(db)

    print("New Password:", new_password)


def offboard():
    username = input("Enter username: ")
    db = load_db()

    if username not in db:
        print("User not found.")
        return

    db[username]["status"] = "DISABLED"
    db[username]["offboarded_date"] = str(datetime.now())

    save_db(db)

    user_dir = os.path.join(BASE_DIR, username)
    archive_dir = os.path.join(BASE_DIR, "Archived")

    os.makedirs(archive_dir, exist_ok=True)

    if os.path.exists(user_dir):
        os.rename(user_dir, os.path.join(archive_dir, username))

    print("User offboarded.")
def onboard():

    first = input("First Name: ")
    last = input("Last Name: ")
    title = input("Job Title: ")
    department = input("Department: ")

    username = (first[0] + last).lower()

    password = "Temp123!"  # simple safe placeholder for now

    db = load_db()

    db[username] = {
        "name": first + " " + last,
        "job_title": title,
        "department": department,
        "password": password,
        "status": "ACTIVE"
    }

    save_db(db)

    user_dir = os.path.join(BASE_DIR, username)
    os.makedirs(user_dir, exist_ok=True)

    print("\nEmployee created:", username)
    print("Temp password:", password)
while True:

    print("\n1. Onboard")
    print("2. View Employees")
    print("3. Reset Password")
    print("4. Offboard Employee")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        onboard()

    elif choice == "2":
        db = load_db()
        print(json.dumps(db, indent=4))

    elif choice == "3":
        reset_password()

    elif choice == "4":
        offboard()

    elif choice == "5":
        break
