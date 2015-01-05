# -*- coding: utf-8 -*-
from django import forms
from models import *
from django.forms.extras.widgets import *
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory

#Formulario de busqueda y filtrado
class BusquedaForm(forms.Form):

	choices_alquiler = (
		('','Venta/Alquiler'),
		('Alquiler', 'Alquiler'), 
		('Compra','Venta'),
	)

	venta_alquiler = forms.ChoiceField(choices=choices_alquiler, required=True, widget=forms.Select())
	categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label=' - Categoria -')
	marca = forms.ModelChoiceField(queryset=Marca.objects.all(), empty_label=' - Marca -')
	estado = forms.ModelChoiceField(queryset=Estado.objects.all(), empty_label=' - Estado -')
	ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), empty_label=' - Ciudad -')
	zona = forms.ModelChoiceField(queryset=Zona.objects.all(), empty_label=' - Zona -')

