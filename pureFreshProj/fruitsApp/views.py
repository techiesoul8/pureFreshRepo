from django.shortcuts import render
from django.http import HttpResponse
from .models import Fruit

from cart.forms import CartAddProductForm
from cart.views import cart_add

# Fruits = [
#     {
#         'author':'ceo',
#         'name':'Soursop' ,
#         'price':'10.00',
#         'description':'Excellent soursop'
#     },
#     {
#         'author': 'chairman',
#         'name': 'Guava',
#         'price': '15.00',
#         'description': 'Yellow onitsha Guava'
#
#     },
# ]

# Create your views here.

cart_product_form = CartAddProductForm()

context = {
    'fruits': Fruit.objects.all(),
    'title': 'Fresh Fruits',
    'cart_product_form': cart_product_form,
}


def home(request):
    response = render(request, 'fruitsApp/base2.html', context)
    return response


def aboutUs(request):
    return HttpResponse('This is the about page')


def check_out(request):
    pass

def my_login(request):
    pass

def products(request):
    pass

def product_details(request):
    pass





