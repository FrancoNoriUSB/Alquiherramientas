# -*- encoding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from models import *
from forms import *


class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'password', 'nombre', 'apellido', 'telefono', 'ciudad', 'nacionalidad', 'cedula')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informacion Personal', {'fields': ('email', 'nombre', 'apellido', 'telefono', 'ciudad', 'nacionalidad', 'cedula')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'apellido', 'telefono', 'ciudad', 'cedula', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    list_filter = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(Banner)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)