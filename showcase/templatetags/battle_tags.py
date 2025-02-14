from random import random

from django import template

register = template.Library()

@register.filter
def get_color(game, choice):
    if not hasattr(game, 'cost'):
        return 'default_color'

    cost_threshold_80 = game.cost * 0.8
    cost_threshold_100 = game.cost
    cost_threshold_200 = game.cost * 2
    cost_threshold_500 = game.cost * 5
    cost_threshold_10000 = game.cost * 100
    cost_threshold_100000 = game.cost * 1000
    cost_threshold_100000000 = game.cost * 1000000

    if choice.value is None:
        # Handle the case where value is None, perhaps by setting a default value
        choice.value = random.randint(0, 1000000)

    if choice.value >= cost_threshold_100000000:
        return 'redgold'
    elif choice.value >= cost_threshold_100000:
        return 'redblack'
    elif choice.value >= cost_threshold_10000:
        return 'black'
    elif choice.value >= cost_threshold_500:
        return 'red'
    elif choice.value >= cost_threshold_200:
        return 'orange'
    elif choice.value >= cost_threshold_100:
        return 'yellow'
    elif choice.value >= cost_threshold_80:
        return 'green'
    else:
        return 'gray'
