from django.test import TestCase
from rango.models import Category

class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        """
        ensure_views_are_positive should results true for categories where views are 0 or positive
        """
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        
self.assertEqual((cat.views >= 0), True)
