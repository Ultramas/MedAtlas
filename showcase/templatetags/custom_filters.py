from django import template

register = template.Library()

@register.filter
def contains_ignore_case(text, substring):
    return substring.lower() in text.lower()


from showcase.views import DirectedTradeOfferView

register = template.Library()

@register.simple_tag
def get_view_method(view, method_name, user):
    method = getattr(view, method_name)
    return method(user)

@register.filter(name='zip')
def zip_lists(a, b):
    return zip(a, b)

@register.filter
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''


@register.filter
def get_color(game, choice):
    if hasattr(game, 'get_color'):
        return game.get_color(choice)
    else:
        raise ValueError("Expected a Game instance, got something else.")

@register.filter
def make_range(value):
    return range(value)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_item(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(str(key)) or dictionary.get(key)
    return None