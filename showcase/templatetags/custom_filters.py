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