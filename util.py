import sqlite3 # Yes I can technically use a csv, no I am not going to use a csv because potentially multiple tables will be created.

#Utility Class for holding key variables
faq_dict = dict()
isUpdated = False

def update_dict(key: str, value: str):
    faq_dict[key] = value
    isUpdated = True

# Populates the dictionary from the db. If there is no data, does an initialization step. Done on startup.
def populate_dict_from_db():
    con = sqlite3.connect("kyrari.db")
    cur = con.cursor()
    # Create Table if first entry
    cur.execute("CREATE TABLE IF NOT EXISTS data(key TEXT PRIMARY KEY, value TEXT)")
    # collect all tables from db.
    res = cur.execute("SELECT * FROM data")
    data = cur.fetchall()
    if len(data) == 0:
        init_db(cur)

    con.close()
    print("Populate success")

def init_db(cur: sqlite3.Cursor):
    print("DB Needs Initializing, initializing now.")
    init_data=[('prifes', 'Please initialise the command'),
               ('coinshop', 'Please initialise the command'),
               ('gachaforecast', 'Please initialise the command'),
               ('gachaguide', 'Please initialise the command')] # eka_commands_key_list = ["prifes", "coinshop", "gachaforecast", "gachaguide"]
    cur.executemany('INSERT INTO data VALUES(?, ?)', init_data)
    print("DB Has been initialized.")

#This function updates the db with the latest values then resets isUpdated to false. 
def update_db():
    if isUpdated:
        con = sqlite3.connect("kyrari.db")
        cur = con.cursor()
        for key in faq_dict:
            cur.exeucte("REPLACE INTO data(key,value) VALUES (?, ?)", (key, faq_dict["key"]))
        con.close()
        isUpdated = False
        print("DB has been updated.")
        # Considering logging on a master discord channel