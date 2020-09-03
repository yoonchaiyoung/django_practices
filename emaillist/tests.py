# from django.test import TestCase
from emaillist import models

# conn() Test
# db = models.conn()
# print(db)

# fetchlist() Test
results = models.fetchlist()
print(results)