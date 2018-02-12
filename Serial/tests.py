from django.test import TestCase
from django.urls import reverse

from Serial.models import Device


# Create your tests here.

def setup(name, sku):
    return Device.objects.create(name=name, SKU=sku, created_by_id=1, maker_id=1, type_id=1, checkout=False)


class IsAnythingHereTest(TestCase):
    def test_nothing(self):
        """Show something if there isn't anything happening in the inventory"""
        response = self.client.get(reverse('device-list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['devices'], [])

    def test_everything(self):
        setup(name="Surface", sku="278wte7ig28364g")
        response = self.client.get(reverse('device-list'))
        self.assertQuerysetEqual(
            response.context['devices'],
            ['<Device: Surface>']
        )
