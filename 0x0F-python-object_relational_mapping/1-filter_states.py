#!/usr/bin/python3
"""
lists all states with a name starting with N from database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id")
    rows = curs.fetchall()
    for r in rows:
        if r[1][0] == 'N':
            print(r)
    curs.close()
    db.close()
