from django.test import TestCase
from django.utils import timezone
from ..forms import EventoForm

class EventoFormTestCase(TestCase):

    def test_data_no_futuro(self):
        data_passada = timezone.now() - timezone.timedelta(days=1)
        dados = {"titulo_do_evento": "evento de teste","data": data_passada,"hora":data_passada.time(),"descricao":"somente para testes"}
        formulario = EventoForm(dados)

        self.assertFalse(formulario.is_valid())
        self.assertIn('data', formulario.errors)
        self.assertIn('A data deve ser no futuro.', formulario.errors['data'])

    def test_falta_titulo(self):
        dados = {"data": timezone.now(),"hora":timezone.now().time(),"descricao":"somente para testes"}
        formulario = EventoForm(dados)

        self.assertFalse(formulario.is_valid())
        self.assertIn('titulo_do_evento',formulario.errors)
        self.assertIn('This field is required.', formulario.errors['titulo_do_evento'])

    def test_falta_data(self):
        dados = {"titulo_do_evento": "evento de teste","hora":timezone.now().time(),"descricao":"somente para testes"}
        formulario = EventoForm(dados)

        self.assertFalse(formulario.is_valid())
        self.assertIn('data',formulario.errors)
        self.assertIn('This field is required.', formulario.errors['data'])

    def test_falta_hora(self):
        dados = {"titulo_do_evento": "evento de teste","data": timezone.now(),"descricao":"somente para testes"}
        formulario = EventoForm(dados)

        self.assertFalse(formulario.is_valid())
        self.assertIn('hora',formulario.errors)
        self.assertIn('This field is required.', formulario.errors['hora'])

    def test_formulario_valido(self):
        dados = {"titulo_do_evento": "evento de teste","data": timezone.now(),"hora":timezone.now().time(),"descricao":"somente para testes"}
        formulario = EventoForm(dados)

        self.assertTrue(formulario.is_valid())
        