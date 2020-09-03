# from django.db import models
from MySQLdb import connect
from MySQLdb.cursors import DictCursor


def fetchlist():
    db = conn()
    cursor = db.cursor(DictCursor)

    sql = 'select no, first_name, last_name, email from emaillist order by no desc'
    cursor.execute(sql)
    results = cursor.fetchall()

    cursor.close()
    db.close()

    return results


def conn():
    return connect(
        user='webdb',
        password='webdb',
        host='192.168.1.138',
        port=3306,
        db='webdb',
        charset='utf8')
