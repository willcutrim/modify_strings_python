from django import forms
from myapp.models import TextoModel

class FormTexto(forms.ModelForm):
    class Meta:
        model = TextoModel
        fields = '__all__'