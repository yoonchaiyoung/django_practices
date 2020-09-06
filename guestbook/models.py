# from django.db import models  (Object Relation Mapping)

from MySQLdb import connect
from MySQLdb.cursors import DictCursor


def fetchlist():
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''select no, 
	                name, 
	                message, 
	                date_format(reg_date, '%Y-%m-%d %h:%i:%s') as reg_date 
                from guestbook
                order by reg_date desc
        '''
    cursor.execute(sql)
    results = cursor.fetchall()

    # 자원 정리
    cursor.close()
    conn.close()

    return results


def getconnection():
    return connect(
        user='webdb',
        password='webdb',
        host='192.168.1.138',
        port=3306,
        db='webdb',
        charset='utf8')
