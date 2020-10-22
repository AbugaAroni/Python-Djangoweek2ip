from django.test import TestCase
from .models import Profile, Friend_Images
# Create your tests here.

class ProfileTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abuga= Profile(user_name = 'Abuga', profilephoto= 'testimage', bio='testbio of this user')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abuga,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.abuga.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.abuga.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.abuga.delete_profile()
        testdelete = Profile.objects.filter(user_name='Abuga')
        self.assertEqual(len(testdelete), 0)

    # Testing update Method
    def test_update_method(self):
        self.abuga.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.abuga.update_profile()
        test_update = Profile.objects.filter(user_name='rick')
        self.assertTrue(len(test_update) > 0)
