from django import forms
from .models import Good


class SeachForm(forms.Form):
    email = forms.EmailField(label='')



class GoodForm(forms.Form):
    name = forms.ModelChoiceField(queryset = Good.objects.all(), label='')


