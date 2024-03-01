# showcase/fields.py
from django import forms
from .models import TradeItem

class UserRestrictedModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(queryset=None, *args, **kwargs)
        self.queryset = TradeItem.objects.filter(user=user)

    def label_from_instance(self, obj):
        return f"{obj.title} - {obj.category}"