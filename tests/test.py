from django.test import TestCase
from apiForm.models import User

class UserTestCase(TestCase):
    def test_fields(self):
        user = User()
        user.name = 'Barack Obama'
        user.email = 'obama@gmail.com'
        user.password = '1234'
        user.type_user = 'User'
        user.save()
        
        record = User.objects.get(pk=1)
        self.assertEqual(record, user)
