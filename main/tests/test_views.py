from django.test import TestCase
from django.urls import reverse
from main import forms

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
        
    def test_contact_us_page_works(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact_form.html')
        self.assertContains(response, 'Cosmetics')
        self.assertIsInstance(response.context["form"], forms.ContactForm)
        
        



