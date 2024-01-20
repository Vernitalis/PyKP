from django.test import TestCase


class HomepageViewTest(TestCase):
    def test_homepage_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTemplateUsed(response, 'logo.html')
        self.assertTemplateUsed(response, 'map.html')
        self.assertTemplateUsed(response, 'side-menu.html')