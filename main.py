import sqlite3
from datetime import datetime, timedelta


conn = sqlite3.connect("db.db")
cursor = conn.cursor() 

today = datetime.today().date()

def check():
    sqlite_select_query = """SELECT * from bdays"""
    cursor.execute(sqlite_select_query)
    everyone = []
    for i in cursor.fetchall():
        days_left = today - datetime.strptime(i[2], "%d.%m.%Y").date()
        print(days_left)



check()
