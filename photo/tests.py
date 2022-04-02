from django.test import TestCase
from .models import Profile,Image
from django.contrib.auth.models import User



class ImageTestCase(TestCase):
   
    def setUp(self):
        self.user = Profile.objects.create_user(username='testuser', password='12345')
        self.image = Image.objects.create(author=self.user, name='test_image', caption='test_caption')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_caption(self):
        self.image.save_image()
        self.image.update_caption('new_caption')
        self.assertTrue(self.image.caption == 'new_caption')