from django.test import TestCase
from accounts.models import User


# Create your tests here.

class UserTest(TestCase):
    def setUp(self):
        User.objects.create(first_name='mahdi',
                            last_name='khaloei',
                            phone_number='09221037478',
                            email='test@test.com')

    def test_get_full_name(self):
        mahdi = User.objects.get(first_name='mahdi')
        self.assertEqual(mahdi.get_full_name(), 'mahdi khaloei')

    def test_get_phone_number(self):
        mahdi = User.objects.get(first_name='mahdi')
        self.assertEqual(mahdi.get_phone_number(), '09221037478')

    def test_get_email(self):
        mahdi = User.objects.get(first_name='mahdi')
        self.assertEqual(mahdi.get_email(), 'test@test.com')

    def test_str_(self):
        mahdi = User.objects.get(first_name='mahdi')
        self.assertEqual(mahdi.__str__(), 'mahdi khaloei')
