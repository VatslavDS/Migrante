
# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.forms import ModelForm


# Create your models here.
class Migrante(models.Model):
	migrante_id = models.AutoField(primary_key=True)
	pseudo = models.CharField(max_length=50)
	de_pais = models.CharField(max_length=50)
	edad = models.IntegerField(default=0)
	genero = models.CharField(max_length=10)
	a_pais = models.CharField(max_length=50)
	timestamp = models.DateTimeField(default=datetime.now)


class PreguntasDelDia(models.Model):
	id_pregunta = models.AutoField(primary_key=True)
	pregunta = models.CharField(max_length=200)
	migrante = models.ForeignKey(Migrante)


class RespuestasDelDia(models.Model):
	id_respuesta = models.ForeignKey(PreguntasDelDia)
	respuesta = models.CharField(max_length=200)


class Abuso(models.Model):
	id_abuso = models.AutoField(primary_key=True)
	abuso = models.CharField(max_length=200)
	migrante = models.ForeignKey(Migrante)
	timestamp = models.DateTimeField(default=datetime.now)



class CheckPoint(models.Model):
	checkpoint_id = models.AutoField(primary_key=True)
	migrante = models.ForeignKey(Migrante)
	longitud = models.IntegerField(default=0)
	latitud = models.IntegerField(default=0)
	ciudad = models.CharField(max_length=100)
	estado = models.CharField(max_length=100)
	pais = models.CharField(max_length=100)
	fechaAvanze = models.DateTimeField(default=datetime.now)
