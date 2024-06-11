from django.test import TestCase
from django.urls import reverse

class TestPage (TestCase):
    def test_home_page_works (self):
        """Test to see if the home page works"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Cosmetics')
        
    def test_home_page_works (self):
        """Test to see if the about page works"""
        response = self.client.get(reverse("about_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')
        self.assertContains(response, 'Cosmetics')
        



