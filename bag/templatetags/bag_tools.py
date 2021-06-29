from django import template


register = template.Library()

""" subtotal calculation. """


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
