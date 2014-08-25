from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory

from .models import Dojo
from .views import ListDojosView

class DojoTests(TestCase):
    """Dojo model tests."""
    
    def test_str(self):
        contact = Dojo(name='Takemusu Aikido')
        self.assertEquals(
            str(contact),
            'Takemusu Aikido',
    )

class DojoListViewTests(TestCase):
    """Dojo list view tests."""
    
    def test_dojos_in_the_context(self): 
      
      client = Client()
      response = client.get('/')
      
      self.assertEquals(list(response.context['object_list']), [])
      
      Dojo.objects.create(name='Aikido Amsterdam')
      response = client.get('/')
      self.assertEquals(response.context['object_list'].count(), 1)
      
    def test_dojos_in_the_context_request_factory(self):
  
        factory = RequestFactory()
        request = factory.get('/')

        response = ListDojosView.as_view()(request)

        self.assertEquals(list(response.context_data['object_list']), [])

        Dojo.objects.create(name='Aikido Sao Paulo')
        response = ListDojosView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)