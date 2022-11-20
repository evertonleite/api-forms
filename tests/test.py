from django.test import TestCase
from apiForm.models import User

class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData")
        pass

    def setUp(self):
        print("setUp")
        pass
    
    def test_fields(self):
        print('1 function test')
        user = User()
        user.name = 'Barack Obama'
        user.email = 'obama@gmail.com'
        user.password = '1234'
        user.type_user = 'User'
        user.save()
        
        record = User.objects.get(pk=1)
        self.assertEqual(record, user)
        
    def test_fields2(self):
        print('2 function test')
        self.assertEqual(1 + 1, 2)
