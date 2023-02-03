from django import forms
from .models import *

class Orderform(forms.ModelForm):
    class Meta:
        model= Order
        fields= '__all__'


class Customerform(forms.ModelForm):
    class Meta:
        model= Customer
        fields= '__all__'