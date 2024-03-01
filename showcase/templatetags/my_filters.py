from django import template
from showcase.models import RespondingTradeOffer

register = template.Library()

@register.filter
def user_offered_trade_items(responding_trade_offer, user):
    return responding_trade_offer.offered_trade_items.filter(user=user)