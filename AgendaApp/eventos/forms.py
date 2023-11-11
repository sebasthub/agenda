from django import forms

class EventoForm(forms.Form):
    titulo_do_evento = forms.CharField(max_length=500, required=True)
    data = forms.DateTimeField(required=True, widget= forms.widgets.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(required=False, widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    descricao = forms.CharField(max_length=50, required=False)