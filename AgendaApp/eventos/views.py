from django.shortcuts import render, get_object_or_404
from .models import Evento

# Create your views here.
def index(request):
    eventos = Evento.objects.all()
    contexto = {
        "eventos": eventos,
    }
    return render(request=request, template_name='index.html',context=contexto)

def evento_detail(request,evento_pk):
    evento = get_object_or_404(Evento, pk=evento_pk)
    contexto = {
        "evento":evento
    }
    return render(request=request, context=contexto, template_name='detail.html')

def evento_cadastro(request):
    if request.method == "POST":
        form = request.POST
        titulo_do_evento = form.get("titulo_evento")
        data_e_hora = form.get("data_hora")
        descricao = form.get("descricao")
        Evento.objects.create(titulo_do_evento=titulo_do_evento,data_e_hora=data_e_hora,descricao=descricao)
        eventos = Evento.objects.all()
        contexto = {
            "eventos": eventos,
        }
        return render(request=request, template_name='index.html',context=contexto)
    else:
        return render(request=request,template_name='cadastro.html')

def evento_editar(request,evento_pk):
    if request.method == "POST":
        form = request.POST
        titulo_do_evento = form.get("titulo_evento")
        data_e_hora = form.get("data_hora")
        descricao = form.get("descricao")
        evento = get_object_or_404(Evento, pk=evento_pk)
        evento.titulo_do_evento = titulo_do_evento
        evento.data_e_hora = data_e_hora
        evento.descricao = descricao
        evento.save()
        eventos = Evento.objects.all()
        contexto = {
            "eventos": eventos,
        }
        return render(request=request, template_name='index.html',context=contexto)
    else:
        evento = get_object_or_404(Evento, pk=evento_pk)
        contexto = {
            "evento":evento
        }
        return render(request=request, context=contexto, template_name='cadastro.html')
    


