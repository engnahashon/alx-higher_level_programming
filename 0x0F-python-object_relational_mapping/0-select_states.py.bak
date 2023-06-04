#!/usr/bin/python3
"""ORM task 0"""
import MySQLdb
from sys import argv


def list_states(username, password, database):
    """"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()
    rows =cur.fetchall()

    for row in rows:
        print(row)
    
    cur.close()
    db.close()

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    list_states(username, password, database)


