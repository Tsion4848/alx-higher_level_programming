#!/usr/bin/python3
"""lists all states from the database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.cursor()
    num_rows = curs.execute("SELECT * FROM states ORDER BY states.id")
    for x in range(num_rows):
        print(curs.fetchone())
