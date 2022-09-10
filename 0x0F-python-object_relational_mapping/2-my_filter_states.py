#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
where name matches the argument
"""

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.cursor()
    query = "SELECT * FROM states WHERE name= '{:s}'\
    ORDER BY states.id".format(argv[4])
    curs.execute(query)
    rows = curs.fetchall()
    for r in rows:
        if r[1] == argv[4]:
            print(r)
    curs.close()
    db.close()
