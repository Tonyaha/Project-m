from django.test import TestCase
from datetime import datetime
from project.apps.users.models import BookInfo

# Create your tests here.  user.has_perm('foo.add_bar')
class TestUsersModels(TestCase):
    def test_users_model(self):
        book = BookInfo(btitle='title-1',bread=10,bcomment=10,isDelete=False)
        book.save()
        #print(book.has_perm('book.add_bar'))
        # for k in book:
        #     print(k, ' ///')
