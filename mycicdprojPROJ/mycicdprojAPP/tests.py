from django.test import TestCase
from . models import Post
# Create your tests here.


class ModelTesting(TestCase):

    # Brings database and fields in for testing
    def setUp(self):
        self.mycicdprojAPP = Post.objects.create(title='django', author='django', slug='django')

    def test_post_model(self):
        d = self.mycicdprojAPP
        # Test if data was entered in db successful
        self.assertTrue(isinstance(d, Post))
        # Test if data was entered in db successful
        self.assertEqual(str(d), 'django')
