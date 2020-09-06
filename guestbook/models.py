# from django.db import models  (Object Relation Mapping)

from MySQLdb import connect
from MySQLdb.cursors import DictCursor


def fetchlist():
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''select no, 
	                name, 
	                message, 
	                date_format(reg_date, '%Y-%m-%d %p %h:%i:%s') as reg_date 
                from guestbook
                order by no desc
        '''
    cursor.execute(sql)
    results = cursor.fetchall()

    # 자원 정리
    cursor.close()
    conn.close()

    return results


def insert(name, password, message):
    conn = getconnection()
    cursor = conn.cursor()

    sql = '''
        insert
            into guestbook
        values (null, %s, %s, %s, now())
    '''
    cursor.execute(sql, (name, password, message))
    conn.commit()

    # 자원 정리
    cursor.close()
    conn.close()

def delete(no, password):
    conn = getconnection()
    cursor = conn.cursor()

    sql = '''
        delete 
        from guestbook 
        where no=%s and password=%s
    '''
    cursor.execute(sql, (no, password))
    conn.commit()

    # 자원 정리
    cursor.close()
    conn.close()


def getconnection():
    return connect(
        user='webdb',
        password='webdb',
        host='192.168.1.138',
        port=3306,
        db='webdb',
        charset='utf8')
