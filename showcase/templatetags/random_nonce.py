from django import template
import random

register = template.Library()

@register.simple_tag
def random_nonce():
    return random.randint(0, 1000000)