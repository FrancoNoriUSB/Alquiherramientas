# -*- encoding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from models import *
from herramientas.apps.main.models import *


# Define el formulario para la creacion de los usuarios
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    cedula = forms.IntegerField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = ('email', 'nombre', 'apellido', 'telefono',  'ciudad', 'nacionalidad', 'cedula', 'is_afiliado')
        widgets = {
                    'telefono': forms.TextInput(),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# Formulario para cambiar el usuario
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'nombre', 'apellido', 'telefono', 'ciudad', 'nacionalidad', 'cedula', 'is_afiliado')

    def clean_password(self):
        return self.initial["password"]


#Formulario de modificacion de contrasena
class modificarContrasenaForm(PasswordChangeForm):

    class Meta(PasswordChangeForm):
        labels = {
        
        }


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


#Formulario de contactos
class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ('telefonos','correo',)
        widgets = {
            'telefonos': forms.Textarea(),
            'correo': forms.Textarea(),
        }


#Formulario de afiliacion
class AfiliacionForm(forms.ModelForm):
    class Meta:
        model = Afiliacion
        fields = ('info','beneficios',)
        widgets = {
            'info': forms.Textarea(),
            'beneficios': forms.Textarea(),
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
        exclude = ['fecha_producto', 'fecha_actualizacion','direccion','herramienta', 'imagen']
        widgets = {
            'titulo': forms.TextInput(),
            'contenido': forms.Textarea(),
            'oferta': forms.CheckboxInput(),
            'precio': forms.NumberInput(),
            'fecha_expiracion': forms.DateInput(attrs={'placeholder':'Formato dd/mm/aaaa'}),
        }


#Formulario para alquilar articulos
class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        exclude = ['fecha_producto', 'fecha_actualizacion','direccion','herramienta', 'imagen']
        widgets = {
            'titulo': forms.TextInput(),
            'contenido': forms.Textarea(),
            'oferta': forms.CheckboxInput(),
            'precio': forms.NumberInput(attrs={'placeholder':'Precio diario'}),
            'fecha_expiracion': forms.DateInput(attrs={'placeholder':'Formato dd/mm/aaaa'}),
        }


#Formulario de imagenes de inmuebles
class ImagenProductoForm(forms.ModelForm):
    class Meta:
        model = ImagenProducto
        exclude = ['Producto', 'thumbnail']
        widgets = {
            'descripcion': forms.TextInput(),
        }


#Formulario para crear la imagen del producto
class ImagenForm(forms.ModelForm):
    class Meta:
        model = ImagenInicial
        exclude = ['thumbnail', 'descripcion']


#Formulario de banners
class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ('nombre', 'imagen', 'url')
        widgets = {
        }

    def clean_imagen(self):
        imagen = self.cleaned_data.get("imagen")
        if not imagen:
            raise forms.ValidationError("Ingrese una imagen.")
        else:
            width, height = get_image_dimensions(imagen)
            if height != 390 :
                raise forms.ValidationError("La altura de la imagen debe exactamente igual a 390 px.")
        return imagen

#Formulario para gestionar los archivos de clausulas
class ClausulasForm(forms.ModelForm):
    class Meta:
        model = Clausula
        fields = ('nombre', 'archivo')
        widgets = {
        }
