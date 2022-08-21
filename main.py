import csv
from datetime import datetime

today = datetime.today().date()

def check():
    friends = []
    with open('db.csv') as f:
        reader = csv.reader(f)
        friend = reader.next()
