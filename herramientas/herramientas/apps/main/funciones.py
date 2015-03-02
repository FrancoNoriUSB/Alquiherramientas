from django.core.mail.message import EmailMessage
from django.core.mail import send_mail
from django.db.models import Count
from django.db.models import Q

#Set de funciones varias a utilizar en el frontend

#Funcion para los correos que se envian en contactanos
def contact_email(request, form):

    emailF = form
    emails = []

    #Informacion del usuario
    name = emailF.cleaned_data['nombre']
    telephone = emailF.cleaned_data['telefono']
    emails.append("evalderrama862@gmail.com")

    #Mensaje a enviar
    message = 'Correo de contacto del usuario: '+ str(name) +'.<br> Con correo: ' + str(emailF.cleaned_data['correo']) +'<br>'
    message += 'Mensaje: '+ str(emailF.cleaned_data['mensaje']) + '<br>'
    message += 'Telefono de contacto: '+ str(telephone)
    send_mail('Correo contacto', message, 'francong2@gmail.com', emails, html_message=message, fail_silently=False)
    return True


#Funcion para los correos de compra de una herramienta.
def email_venta(request, nombre, apellido, telefono, email, herramienta):
    emails = []
    #Informacion del usuario
    emails.append("evalderrama862@gmail.com")

    #Mensaje a enviar
    message = 'El usuario: '+ str(nombre) +' '+ str(apellido) +'.<br> Ha realizado el tramite para la compra de: ' + str(herramienta) +'<br>'
    message += 'Correo de contacto: '+ str(email) + '<br/>'
    message += 'Numero de contacto: '+ str(telefono) + '<br/>'
    subject = "Venta de: "+str(herramienta)
    send_mail(subject, message, 'francong2@gmail.com', emails, html_message=message, fail_silently=False)
    return True

#Funcion para los correos de alquiler de una herramienta.
def email_alquiler(request, nombre, apellido, telefono, email, herramienta, dias):
    emails = []
    #Informacion del usuario
    emails.append("evalderrama862@gmail.com")

    #Mensaje a enviar
    message = 'El usuario: '+ str(nombre) +' '+ str(apellido) +'.<br> Ha realizado el tramite para el alquiler de: ' + str(herramienta) +'<br>'
    message += 'Por '+ str(dias) + ' dias.<br/>'
    message += 'Correo de contacto: '+ str(email) +'<br/>'
    message += 'Numero de contacto: '+ str(telefono) + '<br/>'
    subject = "Alquiler de: "+str(herramienta)
    send_mail(subject, message, 'francong2@gmail.com', emails, html_message=message, fail_silently=False)
    return True

#Funcion para los correos de compra de una herramienta.
def contact_email_producto(request, form, herramienta):

    emailF = form
    emails = []

    #Informacion del usuario
    name = emailF.cleaned_data['nombre']
    telephone = emailF.cleaned_data['telefono']
    emails.append("evalderrama862@gmail.com")

    #Mensaje a enviar
    message = 'Correo de contacto del usuario: '+ str(name) + '.<br/> Enviado mientras veia la herramienta: '+str(herramienta)
    message += '.<br> Con correo: ' + str(emailF.cleaned_data['correo']) +'<br>'
    message += 'Mensaje: '+ str(emailF.cleaned_data['mensaje']) + '<br>'
    message += 'Telefono de contacto: '+ str(telephone)
    send_mail('Correo contacto', message, 'francong2@gmail.com', emails, html_message=message, fail_silently=False)
    return True


#Query dinamico extraido de un proyecto ajeno
def dynamic_query(model, fields, types, values, operator):
    """
     Takes arguments & constructs Qs for filter()
     We make sure we don't construct empty filters that would
        return too many results
     We return an empty dict if we have no filters so we can
        still return an empty response from the view
    """
    
    queries = []
    for (f, t, v) in zip(fields, types, values):
        # We only want to build a Q with a value
        if v != None:
            if t == 'range':
                kwargs = {str('%s__%s' % (f,t)) : (v)}
            else:
                kwargs = {str('%s__%s' % (f,t)) : str('%s' % v)}
            queries.append(Q(**kwargs))
    
    # Make sure we have a list of filters
    if len(queries) > 0:    
        q = Q()
        # AND/OR awareness
        for query in queries:
            if operator == "and":
                q = q & query
            elif operator == "or":
                q = q | query
            else:
                q = None
        if q:
            print q
            # We have a Q object, return the QuerySet
            return model.objects.filter(q)

    else:
        # Return an empty result
        return {}