import random
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django_apscheduler.jobstores import DjangoJobStore
from .models import RubyDrop, RubyDropInstance

RARITY_WEIGHTS = {
    'Common':       700_000,
    'Uncommon':     200_000,
    'Rare':         100_000,
    'Epic':          50_000,
    'Mythical':      30_000,
    'Transcendent': 10_000,
    'Primordial':    7_000,
    'Legendary':     2_900,
    'Ultimate':      100,
    'Final':            1,
}


RARITY_MULTIPLIERS = {
    'Common':       1,
    'Uncommon':     1.2,
    'Rare':         1.5,
    'Epic':         2,
    'Mythical':     3,
    'Transcendent': 5,
    'Primordial':  10,
    'Legendary':   50,
    'Ultimate':  1_000,
    'Final':   1_000_000,
}


def create_instance_for_rubydrop(rubydrop_id):
    rubydrop = RubyDrop.objects.get(pk=rubydrop_id)
    rarities = list(RARITY_WEIGHTS.keys())
    weights  = list(RARITY_WEIGHTS.values())
    selected = random.choices(rarities, weights=weights, k=1)[0]

    multiplier = RARITY_MULTIPLIERS[selected]
    instance_amount = int(rubydrop.amount * multiplier)

    RubyDropInstance.objects.create(
        rubydrop=rubydrop,
        amount=instance_amount,
        rarity=selected,
        opentime=rubydrop.opentime,
        is_active=rubydrop.is_active,
    )
