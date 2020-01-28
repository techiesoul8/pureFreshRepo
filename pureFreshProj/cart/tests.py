from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.views import cart_add, cart_detail, cart_remove
# Create your tests here.


class TestUrls(SimpleTestCase):
    def test_cart_details_url_resolves(self):
        url = reverse('cart:cart_detail')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, cart_detail)

    def test_cart_