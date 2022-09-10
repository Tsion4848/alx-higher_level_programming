#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.cursor()
    query = "SELECT cities.name FROM cities JOIN states ON\
    cities.state_id = states.id WHERE states.name=%s\
    ORDER BY cities.id"
    num_rows = curs.execute(query, (argv[4],))
    rows = curs.fetchall()
    res = []
    x = 0
    for r in rows:
        res.append(rows[x][0])
        x += 1
    join = ", ".join(res)
    print(join)
    curs.close()
    db.close()
