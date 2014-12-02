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
from models import *
from forms import *
from django.core.mail.message import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_countries import countries

def home(request):

	ctx = {

	}

	return render_to_response('main/home/home.html', ctx, context_instance=RequestContext(request))