from django.shortcuts import render

from .views_customers import *
from .views_products import *
from .views_discounts import *
from .views_shippings import *
from .views_orders import *
from .views_payments import *
from .views_wishlist import *


def homepage(request):
    return render(request, template_name='core/homepage.html')
