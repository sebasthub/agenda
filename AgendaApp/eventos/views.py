from django.shortcuts import render
from .models import Evento

# Create your views here.
def index(request):
    eventos = Evento.objects.all()
    contexto = {
        "eventos": eventos,
    }
    return render(request=request, template_name='index.html',context=contexto)
