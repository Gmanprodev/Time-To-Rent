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
        'stripe_public_key': 'pk_test_51J2FVBIqm6PsxWlBfudP1Ry0DOMHGBtJeHRFExil52OiRd7NutruAvmxlhRXALDC5TG19F9KR2l45Zd8On7aL8DH00u95DtfWo'
    }

    return render(request, template, context)
