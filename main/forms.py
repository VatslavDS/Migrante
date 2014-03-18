# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from models import Migrante, PreguntasDelDia, RespuestasDelDia, Abuso, CheckPoint

class MigranteSearch(forms.Form):
	pseudo = forms.CharField(max_length=50)


class MigranteForm(ModelForm):
	class Meta:
		model = Migrante
		fields = ['pseudo', 'de_pais', 'edad', 'genero', 'a_pais']
	
class PreguntasDelDiaForm(ModelForm):
	class Meta:
		model = PreguntasDelDia
		fields = ['pregunta', 'migrante']

class RespuestasDelDiaForm(ModelForm):
	class Meta:
		model = RespuestasDelDia
		fields = ['id_respuesta', 'respuesta']

class AbusoForm(ModelForm):
	class Meta:
		model = Abuso
		fields = ['abuso', 'migrante']

class CheckPointForm(ModelForm):
	class Meta:
		model = CheckPoint
		fields = ['pseudo', 'longitud', 'latitud', 'ciudad', 'estado', 'pais']	