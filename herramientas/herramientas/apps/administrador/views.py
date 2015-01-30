# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from datetime import datetime, date
from django.db.models import Count
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import *
from forms import *
from herramientas.apps.main.models import *
from herramientas.apps.administrador.forms import *
import json

#Vista del inicio
def inicio(request):

    ctx={

    }

    return render_to_response('administrador/inicio/inicio.html', ctx, context_instance=RequestContext(request))
