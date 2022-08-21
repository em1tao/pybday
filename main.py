import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta
from termcolor import colored

conn = sqlite3.connect("db.db")
cursor = conn.cursor() 

today = datetime.today().date()

def validate(date_text: str):
    try:
        datetime.strptime(date_text, '%d.%m.%Y')
        return True
    except:
        return False

def check():
    sqlite_select_query = """SELECT * from bdays"""
    cursor.execute(sqlite_select_query)
    for i in cursor.fetchall():
        bday = datetime.strptime(i[2], "%d.%m.%Y").date()
        next_age = today.year - bday.year
        this_year_bday = datetime.strptime(f"{i[2][0:6]}{today.year}", "%d.%m.%Y").date()
        days_left = (this_year_bday - today).days
        if days_left == 0:
            days_left = 'Today!'
        elif days_left < 0:
            this_year_bday += relativedelta(years=1)
            next_age += 1
            days_left = (this_year_bday - today).days
        print(i[0], i[1], days_left, next_age)

def add_new(name: str, birthdate: str):
    sqlite_insert_query = """INSERT INTO bdays 
                             (name, birthdate)
                             VALUES (?,?)"""
    if len(name) > 15:
        print(colored("[+] Name has to be at most 15 characters", "red"))
        return

    if validate(birthdate):
        cursor.execute(sqlite_insert_query, (name, birthdate))
        conn.commit()
        print(colored("[+] Success!", "green"))
    else:
        print(colored("Incorrect data format, should be DD.MM.YYYY", "red"))

def remove(id: str):
    sqlite_remove_query = """DELETE FROM bdays WHERE id=?"""
    try:
        cursor.execute(sqlite_remove_query, (id))
        conn.commit()
        print(colored("[+] Success!", "green"))
    except sqlite3.ProgrammingError:
        print(colored("[+] Error", "red"))

check()
