from django.shortcuts import render, get_object_or_404
from .models import Evento
from .forms import EventoForm
from datetime import datetime, time

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

def evento_cadastrar(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            titulo_do_evento = form.cleaned_data["titulo_do_evento"]
            data = form.cleaned_data["data"]
            hora = form.cleaned_data["hora"]
            data_e_hora = datetime.combine(data,hora)
            descricao = form.cleaned_data["descricao"]
            Evento.objects.create(titulo_do_evento=titulo_do_evento,data_e_hora=data_e_hora,descricao=descricao)
            eventos = Evento.objects.all()
            contexto = {
                "eventos": eventos,
            }
            return render(request=request, template_name='index.html',context=contexto)
    else:
        form = EventoForm()
        contexto = {
            "form": form
        }
        return render(request=request,template_name='cadastro.html', context=contexto)

def evento_editar(request,evento_pk):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = get_object_or_404(Evento, pk=evento_pk)
            evento.titulo_do_evento = form.data["titulo_do_evento"]
            data = form.cleaned_data["data"]
            hora = form.cleaned_data["hora"]
            evento.data_e_hora = datetime.combine(data,hora)
            evento.descricao = form.data["descricao"]
            evento.save()
            eventos = Evento.objects.all()
            contexto = {
                "eventos": eventos,
            }
        return render(request=request, template_name='index.html',context=contexto)
    else:
        evento = get_object_or_404(Evento, pk=evento_pk)
        form = EventoForm({"titulo_do_evento":evento.titulo_do_evento,"data":evento.data_e_hora.date(),"hora":evento.data_e_hora.time(),"descricao": evento.descricao})
        contexto = {
            "form":form
        }
        return render(request=request, context=contexto, template_name='cadastro.html')
    

def evento_excluir(request,evento_pk):
    evento = get_object_or_404(Evento, pk=evento_pk)
    evento.delete()
    eventos = Evento.objects.all()
    contexto = {
        "eventos": eventos,
    }
    return render(request=request, template_name='index.html',context=contexto)

