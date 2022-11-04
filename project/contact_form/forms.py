from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'post'
        self.helper.form_action = '/contact'

        self.helper.add_input(Submit('submit', 'Submit'))
        
    email = forms.EmailField(max_length=254)
    message = forms.CharField(max_length=254, widget=forms.Textarea)