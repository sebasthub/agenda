"""
URL configuration for AgendaApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eventos.views import index, evento_detail, evento_cadastrar, evento_editar,evento_excluir

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('evento/<int:evento_pk>/', evento_detail, name='detalhes_do_evento'),
    path('evento/cadastro/', evento_cadastrar, name='cadastra_evento'),
    path('evento/edita/<int:evento_pk>/', evento_editar, name='editar_evento'),
    path('evento/exclui/<int:evento_pk>/', evento_excluir, name='excluir_evento')
]
