# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import *
from forms import MigranteSearch, MigranteForm, PreguntasDelDiaForm, RespuestasDelDiaForm, AbusoForm, CheckPointForm
from django.template import RequestContext
from django.core.mail import EmailMessage

# Create your views here.
#Implementar formulario
def buscarUsuario(request):
	if request.method == 'POST':
		formulario_migrante = MigranteSearch(request.POST)
		print request.POST
		if formulario_migrante.is_valid():
			pseudo = formulario_migrante.cleaned_data['pseudo']
			try:
				datos_migrante = Migrante.objects.get(pseudo=pseudo)
			except:
			    datos_migrante = None
			return render_to_response('main.html', {'migrante' : datos_migrante})
	else:
		formulario_migrante = MigranteSearch()
	return render_to_response('index.html', {'formulario' : formulario_migrante}, context_instance=RequestContext(request))


def registroMigrante(request):
	if request.method == 'POST':
		formulario_registro = MigranteForm(request.POST)
		if formulario_registro.is_valid():
			formulario_registro.save()
			pseudo = formulario_registro.cleaned_data['pseudo']
			datos_migrante = Migrante.objects.get(pseudo=pseudo)
			return render_to_response('main.html', {'migrante' : datos_migrante})
	else:
		formulario_registro = MigranteForm()
	return render_to_response('registro.html', {'formulario' : formulario_registro}, context_instance=RequestContext(request))


def checkPoint(request):
	if request.method == 'POST':
		formulario_checkpoint = CheckPointForm(request.POST)
		if formulario_checkpoint.is_valid():
			formulario_checkpoint.save()
			#Ver el manejo de la sesión del usuario
			return render_to_response('main.html')				
	else:
		formulario_checkpoint = CheckPointForm()
	return render_to_response('checkpoint.html', {'formulario' : formulario_checkpoint}, context_instance=RequestContext(request))

def main(request):
	return render_to_response('main.html')
