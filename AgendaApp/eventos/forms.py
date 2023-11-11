from django import forms
from django.utils import timezone

def valida_data_futura(value):
        if value < timezone.now() - timezone.timedelta(days=1):
            raise forms.ValidationError('A data deve ser no futuro.')

class EventoForm(forms.Form):
    titulo_do_evento = forms.CharField(max_length=500, required=True)
    data = forms.DateTimeField(required=True, widget= forms.widgets.DateInput(attrs={'type': 'date'}), validators=[valida_data_futura])
    hora = forms.TimeField(required=True, widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    descricao = forms.CharField(max_length=50, required=False)
    