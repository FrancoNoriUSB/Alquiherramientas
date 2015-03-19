from django.core.mail.message import EmailMessage
from django.core.mail import send_mail
from django.db.models import Count
from django.db.models import Q


#Funcion para manejar los archivos que se suben
def handle_uploaded_file(f, nombre):

	with open('/', 'w') as destination:
		for chunk in f.chunks():
			destination.write(chunk)