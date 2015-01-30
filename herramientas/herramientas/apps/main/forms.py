# -*- coding: utf-8 -*-
from django import forms
from models import *
from django.forms.extras.widgets import *
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory

#Formulario de busqueda y filtrado
class BusquedaForm(forms.Form):

	choices_alquiler = (
		('','- Venta/Alquiler -'),
		('alquiler', 'Alquiler'), 
		('venta','Venta'),
	)

	tipo = forms.ChoiceField(choices=choices_alquiler, widget=forms.Select(), required=False)
	categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label=' - Categoria -', required=False)
	marca = forms.ModelChoiceField(queryset=Marca.objects.all(), empty_label=' - Marca -', required=False)
	estado = forms.ModelChoiceField(queryset=Estado.objects.all(), empty_label=' - Estado -', required=False)
	ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), empty_label=' - Ciudad -', required=False)
	zona = forms.ModelChoiceField(queryset=Zona.objects.all(), empty_label=' - Zona -', required=False)


#Formulario para contactar a la empresa
class ContactoForm(forms.Form):
	remitente = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)