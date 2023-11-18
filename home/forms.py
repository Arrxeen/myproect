from django import forms
from home.models import Slot


class SlotForm(forms.ModelForm):
    class Meta:
        model =Slot
        fields = ['name','size','link','price','category']

