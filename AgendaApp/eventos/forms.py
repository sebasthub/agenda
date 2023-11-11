from django import forms
from django.utils import timezone

class EventoForm(forms.Form):
    titulo_do_evento = forms.CharField(max_length=500, required=True)
    data = forms.DateTimeField(required=True, widget= forms.widgets.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(required=False, widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    descricao = forms.CharField(max_length=50, required=False)
    def clean_data(self):
        data = self.cleaned_data.get('data')
        if data and data <= timezone.now():
            raise forms.ValidationError("A data deve ser no futuro.")
        return data