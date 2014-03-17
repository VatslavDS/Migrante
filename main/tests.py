from django.test import TestCase
from models import Migrante, PreguntasDelDia, RespuestasDelDia, Abuso, CheckPoint


# Create your tests here.
class FormTestingCase(TestCase):
	fixtures = ['migrante_fixture.json']

	def setUp(self):
		super(FormTestingCase, self).setUp()

	def test_init(self):
		#Test succesful init without data.
		form = 