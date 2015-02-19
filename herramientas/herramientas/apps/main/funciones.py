from django.core.mail.message import EmailMessage
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
    emails.append("info@menu2cero.com")

    #Mensaje a enviar
    message = 'Correo de contacto del usuario: '+ str(name) +'.<br> Con correo: ' + str(emailF.cleaned_data['correo']) +'<br>'
    message += 'Mensaje: '+ str(emailF.cleaned_data['mensaje']) + '<br>'
    message += 'Telefono de contacto: '+ str(telephone)
    send_mail('[Menu2Cero] Correo contacto', message, 'info@menu2cero.com', emails, html_message=message, fail_silently=False)
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
            if t == 'precio__range':
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