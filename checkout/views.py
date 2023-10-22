from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O4A1QFArSwfkDB3D0kUFOPQ8p4m7yfL1yUtB3f\
            EARjJE2xK8pFHKfeLGO46nJn54TtLSsRUtNbBn30Dq3ro2lZi00BJdKZYSp',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
