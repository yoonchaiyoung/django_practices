# from django.test import TestCase (Django TDO)
import guestbook.models as guestbookmodel

# results = guestbookmodel.fetchlist()
# print(results)

def test_guestbookmodel_insert():
    guestbookmodel.insert('윤채영', '1234', '안녕하세요~')



def test_guestbookmodel_fetchlist():
    results = guestbookmodel.fetchlist()
    print(results)


# test_guestbookmodel_fetchlist()
test_guestbookmodel_insert()
