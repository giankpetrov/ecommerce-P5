from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ View to return all productos, sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
