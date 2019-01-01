from django.test import TestCase
from datetime import datetime
import unittest
from project.apps.users.models import Users
#from project.apps.users.models import BookInfo

@unittest.skip
# Create your tests here.  user.has_perm('foo.add_bar')
class TestUsersModels(TestCase):
    def test_users_model(self):
        book = BookInfo(btitle='title-1',bread=10,bcomment=10,isDelete=False)
        book.save()
        #print(book.has_perm('book.add_bar'))
        # for k in book:
        #     print(k, ' ///')


class TestUsersModel(TestCase):
    def test_create(self):
        # user = Users.create('xmzd')
        # print(user.name)
        pass
