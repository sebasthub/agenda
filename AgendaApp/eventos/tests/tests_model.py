from django.test import TestCase
from ..models import Evento
from django.utils import timezone
from django.core.exceptions import ValidationError

class EventoTestCase(TestCase):
    
    def setUp(self) -> None:
        Evento.objects.create(titulo_do_evento='evento teste',data_e_hora='2023-11-11 18:30',descricao='só um teste')
    
    def test_retorno_str(self):
        evento = Evento.objects.get(titulo_do_evento='evento teste')
        self.assertEquals(evento.__str__(), 'evento teste')

    def test_tem_todos_os_campos(self):
        evento = Evento.objects.get(titulo_do_evento='evento teste')
        self.assertEquals(evento.titulo_do_evento, 'evento teste')
        self.assertEquals(evento.data_e_hora.__str__(), '2023-11-11 18:30:00+00:00')
        self.assertEquals(evento.descricao, 'só um teste')
