from django import forms
from django.forms import ModelForm
from .models import *

class SiswaForm(ModelForm):

    class Meta:
        model = Siswa
        fields = '__all__'
        widgets = {
            'niup': forms.TextInput(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
        }
        