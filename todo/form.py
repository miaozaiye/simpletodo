from django import forms
from django.core.exceptions import ValidationError

class NewForm(forms.Form):
    item = forms.CharField(max_length=100)
    item_status = 'new'


class DoneForm(forms.Form):
    id = forms.IntegerField()
    item_status = 'done'
