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

	choices_precio = (
		('','- Precio -'),
		('0-10000','0-10.000'),
		('10000-50000','10.000 - 50.000'),
		('50000-200000','50.000 - 200.000'),
		('200000-1000000','200.000 - 1.000.000'),
		('1000000-10000000','1.000.000 - 10.000.000'),
		('10000000-10000000000000000','10.000.000 - más'),
	)

	tipo = forms.ChoiceField(choices=choices_alquiler, widget=forms.Select(), required=True)
	categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label=' - Categoria -', required=False)
	marca = forms.ModelChoiceField(queryset=Marca.objects.all(), empty_label=' - Marca -', required=False)
	estado = forms.ModelChoiceField(queryset=Estado.objects.all(), empty_label=' - Estado -', required=False)
	ano = forms.ModelChoiceField(queryset=Herramienta.objects.all().values_list('ano', flat=True).distinct().order_by('ano'), empty_label=' - Año -', required=False)
	precio = forms.ChoiceField(choices=choices_precio, widget=forms.Select(), required=False)


#Formulario para contactar a la empresa
class ContactoForm(forms.Form):
	nombre = forms.CharField(required=True)
	telefono = forms.CharField(required=True)
	correo = forms.EmailField(required=True)
	mensaje = forms.CharField(widget=forms.Textarea, required=True)


#Formulario para comprar articulos
class CompraForm (forms.Form):
	precio = forms.IntegerField(required=True)
	total = forms.IntegerField(required=True)
	clausulas = forms.BooleanField(required=True)


#Formulario para alquilar articulos
class AlquilerForm(forms.Form):
	precioA = forms.IntegerField(required=True)
	diasA = forms.IntegerField(required=True)
	totalA = forms.IntegerField(required=True)
	clausulasA = forms.BooleanField(required=True)
