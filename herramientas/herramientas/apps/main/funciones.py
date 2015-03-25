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
    email = emailF.cleaned_data['correo']
    emails.append(email)
    emails.append('contacto@alquiherramientas.com')

    #Mensaje a enviar
    message = 'Correo de contacto del usuario: '+ str(name) +'.<br> Con correo: ' + str(email) +'<br>'
    message += 'Mensaje: '+ str(emailF.cleaned_data['mensaje']) + '<br>'
    message += 'Telefono de contacto: '+ str(telephone)

    email = EmailMessage()
    email.subject = '[Alquiherramientas] Correo contacto'
    email.body = message
    email.from_email = 'contacto@alquiherramientas.com'
    email.to = emails
    email.content_subtype = "html"
    enviado=email.send()
    return True

#Funcion para los correos de compra de una herramienta.
def email_venta(request, nombre, apellido, telefono, email, herramienta, cantidad):
    emails = []
    #Informacion del usuario
    emails.append(email)
    emails.append('ventas@alquiherramientas.com')

    #Mensaje a enviar
    message = 'El usuario: '+ str(nombre) +' '+ str(apellido) +'.<br>'
    message += 'Ha realizado el tramite para la compra de: ' + str(herramienta) +'<br>'
    message += 'Cantidad: '+ str(cantidad) + '<br/>'
    message += 'Correo de contacto: '+ str(email) + '<br/>'
    message += 'Numero de contacto: '+ str(telefono) + '<br/>'
    message += 'El usuario acepto las clausulas.'

    email = EmailMessage()
    email.subject = '[Alquiherramientas] Nueva Venta'
    email.body = message
    email.from_email = 'ventas@alquiherramientas.com'
    email.to = emails
    email.content_subtype = "html"
    enviado=email.send()
    return True


#Funcion para los correos de alquiler de una herramienta.
def email_alquiler(request, nombre, apellido, telefono, email, herramienta, dias, cantidad):
    emails = []
    #Informacion del usuario
    emails.append(email)
    emails.append('alquiler@alquiherramientas.com')

    #Mensaje a enviar
    message = 'El usuario: '+ str(nombre) +' '+ str(apellido) +'.<br>'
    message += 'Ha realizado el tramite para el alquiler de: ' + str(herramienta) +'<br>'
    message += 'Cantidad: '+ str(cantidad) + '<br/>'
    message += 'Por '+ str(dias) + ' dias.<br/>'
    message += 'Correo de contacto: '+ str(email) +'<br/>'
    message += 'Numero de contacto: '+ str(telefono) + '<br/>'
    message += 'El usuario acepto las clausulas.'
    subject = "Alquiler de: "+str(herramienta)

    email = EmailMessage()
    email.subject = '[Alquiherramientas] Nuevo Alquiler'
    email.body = message
    email.from_email = 'alquiler@alquiherramientas.com'
    email.to = emails
    email.content_subtype = "html"
    enviado=email.send()
    return True


#Funcion para los correos de compra de una herramienta.
def contact_email_producto(request, form, herramienta, id_producto):

    emailF = form
    emails = []

    #Informacion del usuario
    name = emailF.cleaned_data['nombre']
    telephone = emailF.cleaned_data['telefono']
    email = emailF.cleaned_data['correo']
    emails.append(email)
    emails.append('contacto@alquiherramientas.com')

    #Mensaje a enviar
    message = 'Correo de contacto del usuario: '+ str(name) + '.<br/> Enviado mientras veia la herramienta: <a href="www.alquiherramientas.com/productos/'+str(id_producto)+' target="new">'+str(herramienta)+'"</a>'
    message += '.<br> Con correo: ' + str(emailF.cleaned_data['correo']) +'<br>'
    message += 'Mensaje: '+ str(emailF.cleaned_data['mensaje']) + '<br>'
    message += 'Telefono de contacto: '+ str(telephone)

    email = EmailMessage()
    email.subject = '[Alquiherramientas] Contacto de producto'
    email.body = message
    email.from_email = 'contacto@alquiherramientas.com'
    email.to = emails
    email.content_subtype = "html"
    enviado=email.send()
    return True
    return True


# Funcion para enviar correo cuando se agota un producto.
def email_agotado(request, producto):
    emails = []
    emails.append("ventas@alquiherramientas.com")
    emails.append("alquiler@alquiherramientas.com")

    #Mensaje a enviar
    message = 'El producto: '+ str(producto.titulo) + ' se ha agotado.'
    message += 'Visitar en el admin, <a href="www.alquiherramientas.com/administrador/">Producto</a>'

    email = EmailMessage()
    email.subject = '[Alquiherramientas] Producto Agotado'
    email.body = message
    email.from_email = 'contacto@alquiherramientas.com'
    email.to = emails
    email.content_subtype = "html"
    enviado=email.send()
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