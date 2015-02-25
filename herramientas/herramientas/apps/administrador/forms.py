# -*- encoding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from models import *
from herramientas.apps.main.models import *


# Define el formulario para la creacion de los usuarios
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    cedula = forms.IntegerField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = ('email', 'nombre', 'apellido', 'ciudad', 'nacionalidad', 'cedula')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# Formulario para cambiar el usuario
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'nombre', 'apellido', 'ciudad', 'nacionalidad', 'cedula')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
        

#Formulario para el login de usuario                
class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email','password')
        widgets = {
            'password': forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Contraseña"}),
            'email': forms.EmailInput(attrs={'class':"form-control", 'placeholder':"Correo"}),
        }


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('info', 'mision', 'vision', 'servicios')
        widgets = {
            'info':forms.Textarea(),
            'mision':forms.Textarea(),
            'vision':forms.Textarea(),
            'servicios':forms.Textarea(),
        }


#Formulario de empresa
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('info','mision','vision','servicios')
        widgets = {
            'info': forms.Textarea(),
            'mision': forms.Textarea(),
            'vision': forms.Textarea(),
            'servicios': forms.Textarea(),
        }


#Formulario de categorias
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)


#Formulario de marcas
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('nombre',)


#Formulario de modelos
class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ('nombre','marca',)


#Formulario de Estados
class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ('nombre',)
    

#Formulario de ciudades
class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ('nombre', 'estado')
    

#Formulario de zonas
class ZonaForm(forms.ModelForm):
    class Meta:
        model = Zona
        fields = ('nombre', 'ciudad')


#Formulario de herramienta
class HerramientaForm(forms.ModelForm):
    class Meta:
        model = Herramienta
        fields = ('nombre','ano','categoria','marca','modelo',)


#Formulario de direccion
class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ('domicilio','estado','ciudad','zona',)


#Formulario para vender articulos
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        exclude = ['fecha_producto', 'fecha_actualizacion','direccion','herramienta']
        widgets = {
            'titulo': forms.TextInput(),
            'contenido': forms.Textarea(),
            'imagen': forms.FileInput(),
            'oferta': forms.CheckboxInput(),
            'precio': forms.NumberInput(),
            'fecha_expiracion': forms.DateInput(attrs={'placeholder':'Formato dd/mm/aaaa'}),
        }


#Formulario para alquilar articulos
class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        exclude = ['fecha_producto', 'fecha_actualizacion','direccion','herramienta']
        widgets = {
            'titulo': forms.TextInput(),
            'contenido': forms.Textarea(),
            'imagen': forms.FileInput(),
            'oferta': forms.CheckboxInput(),
            'precio': forms.NumberInput(attrs={'placeholder':'Precio diario'}),
            'fecha_expiracion': forms.DateInput(attrs={'placeholder':'Formato dd/mm/aaaa'}),
        }


#Formulario de banners
class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ('nombre', 'imagen', 'url')