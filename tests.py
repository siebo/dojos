from django.test import TestCase

from .models import Dojo

class DojoTests(TestCase):
    """Dojo model tests."""
    
    def test_str(self):
        contact = Dojo(name='Takemusu Aikido')
        self.assertEquals(
            str(contact),
            'Takemusu Aikido',
    )
