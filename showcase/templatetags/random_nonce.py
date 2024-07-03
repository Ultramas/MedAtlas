from django import template
import random

register = template.Library()

@register.simple_tag
def random_nonce():
    return random.randint(0, 1000000)


@register.filter
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''


@register.filter
def get_color(game, choice):
    return game.get_color(choice)