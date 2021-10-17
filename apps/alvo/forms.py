from django import forms

from .models import Alvo


class AlvoModelForm(forms.ModelForm):
    class Meta:
        model = Alvo
        fields = ['nome', 'latitude', 'longitude', 'data_expiracao']


