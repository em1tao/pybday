import sqlite3
from datetime import datetime


conn = sqlite3.connect("db.db")
cursor = conn.cursor() 

today = datetime.today().date()

GREEN = "\033[32m"
RED = "\033[31m"
WHITE = "\033[m"


def validate(date_text: str):
    try:
        a = datetime.strptime(date_text, '%d.%m.%Y').date()
        return a < today
    except:
        return False

header = \
"""\
┌────┰───────────────┰──────────┰─────────────┰────────────┐
│ id │      Name     │   Date   │  Days left  │  Next age  │"""

def check(): 
    print(header)
    sqlite_select_query = """SELECT * from bdays"""
    cursor.execute(sqlite_select_query)
    for i in cursor.fetchall():
        print("├────┼───────────────┼──────────┼─────────────┼────────────┤")
        bday = datetime.strptime(i[2], "%d.%m.%Y").date()
        next_age = today.year - bday.year
        this_year_bday_str = f"{i[2][0:6]}{today.year}"
        this_year_bday = datetime.strptime(this_year_bday_str, "%d.%m.%Y").date()
        days_left = (this_year_bday - today).days
        if days_left == 0:
            days_left = 'Today!'
        elif days_left < 0:
            next_age += 1
            this_year_bday_str = this_year_bday_str[:-4] + str(today.year+1) 
            this_year_bday = datetime.strptime(this_year_bday_str, "%d.%m.%Y").date()
            days_left = (this_year_bday - today).days
            
        next_age = str(next_age)
        days_left = str(days_left)
        id = str(i[0]) if i[0] > 10 else "0"+str(i[0])
        print(f"\r│{id.center(4)}│{i[1].center(15)}│{i[2]}│{days_left.center(13)}│{next_age.center(12)}│")
    print("└────┴───────────────┴──────────┴─────────────┴────────────┘")
def add_new(name: str, birthdate: str):
    sqlite_insert_query = """INSERT INTO bdays 
                             (name, birthdate)
                             VALUES (?,?)"""
    if len(name) > 15:
        print(RED+"[+] Name has to be at most 15 characters")
        return

    if validate(birthdate):
        cursor.execute(sqlite_insert_query, (name, birthdate))
        conn.commit()
        print(GREEN+"[+] Success!")
    else:
        print(RED+"[+] Incorrect data format, should be DD.MM.YYYY")

def remove(id: str):
    sqlite_remove_query = """DELETE FROM bdays WHERE id=?"""
    if id[0] == '0':
        id = id[1:]
    try:
        cursor.execute(sqlite_remove_query, (id))
        conn.commit()
        print(GREEN+"[+] Success!")
    except sqlite3.ProgrammingError:
        print(RED+"[+] Error")

