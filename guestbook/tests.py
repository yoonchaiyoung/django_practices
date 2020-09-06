# from django.test import TestCase (Django TDO)
import guestbook.models as guestbookmodel

# results = guestbookmodel.fetchlist()
# print(results)

def test_guestbookmodel_fetchlist():
    results = guestbookmodel.fetchlist()
    print(results)


test_guestbookmodel_fetchlist()
