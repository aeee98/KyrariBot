import sqlite3 # Yes I can technically use a csv, no I am not going to use a csv because potentially multiple tables will be created.

#Utility Class for holding key variables
faq_dict = dict()
isUpdated = False

def update_dict(key: str, value: str):
    faq_dict[key] = value
    isUpdated = True

def populate_dict_from_db():
    con = sqlite3.connect("kyrari.db")
    cur = con.cursor()
    # Create Table if first entry
    cur.execute("CREATE TABLE IF NOT EXISTS data(key, value)")
    # collect all tables from db.
    res = cur.execute("SELECT * FROM data")
    data = cur.fetchall()
    if len(data) == 0:
        init_db(cur)
    print("Populate success")

def init_db(cur: sqlite3.Cursor):
    print("DB Needs Initializing, initializing now.")
    

    print("DB Has been initialized.")

#This function updates the db with the latest values then resets isUpdated to false.
def update_db():
    if isUpdated:
        isUpdated = False
        print("DB has been updated.")
        # Considering logging on a master discord channel