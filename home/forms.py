from django import forms
from django.forms import TextInput

from .models import Data


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"


class NormalisasiForm(forms.Form):
    sigma = forms.CharField(label='Sigma', required=True, max_length=100,
                            widget=TextInput(attrs={'type': 'number'}),
                            error_messages={'required': "Sigma"})

class TrainingForm(forms.Form):
    lamda = forms.CharField(label='Lambda', required=True, max_length=100,
                             widget=TextInput(attrs={'type': 'number'}),
                             error_messages={'required': "Lambda"})
    constant = forms.CharField(label='Constant', required=True, max_length=100,
                                widget=TextInput(attrs={'type': 'number'}),
                                error_messages={'required': "Constant"})
    gamma = forms.CharField(label='Gamma', required=True, max_length=100,
                             widget=TextInput(attrs={'type': 'number'}),
                             error_messages={'required': "Gamma"})
    iterasi = forms.CharField(label='Iterasi', required=True, max_length=100,
                               widget=TextInput(attrs={'type': 'number'}),
                               error_messages={'required': "Iterasi"})

