from django.test import TestCase
from authapp.models import login,Register


# Create your tests here.
class loginTestCase(TestCase):
    def setUp(self):
        login.objects.create(username="manaswini")

    def test_sigup_info(self):
        c1 = login.objects.get(username="manaswini")
        self.assertEqual(c1.get_user(), "manaswini")
        # self.assertEqual()


class SignupTestCase(TestCase):
    def setUp(self):
        Register.objects.create(fname="Manaswini Patra",phno="8093841334",email="patra.manaswini123@gmail.com",uname="manaswini",pwd="123456789",cpwd="123456789")

    def test_sigup_info(self):
        c1 = Register.objects.get(fname="Manaswini Patra")
        self.assertEqual(c1.get_fname(), "Manaswini Patra")
