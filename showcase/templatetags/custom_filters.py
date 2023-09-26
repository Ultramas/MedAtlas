from django import template

register = template.Library()

@register.filter
def contains_ignore_case(text, substring):
    return substring.lower() in text.lower()
