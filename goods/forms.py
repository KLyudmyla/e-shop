from django import forms
from .models import Good


class SeachForm(forms.Form):
    email = forms.CharField(label='email')

class GoodForm(forms.Form):
    name = forms.ModelChoiceField(queryset = Good.objects.all() )

