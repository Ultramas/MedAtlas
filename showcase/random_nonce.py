from django import template
import random

register = template.Library()

@register.simple_tag
def random_nonce(choice):
    lower_nonce = random.randint(1, 1000)  # Example range
    upper_nonce = random.randint(1001, 2000)  # Example range
    return {
        'nonce': random.randint(lower_nonce, upper_nonce),
        'choice': choice,
        'lower_nonce': lower_nonce,
        'upper_nonce': upper_nonce
    }
