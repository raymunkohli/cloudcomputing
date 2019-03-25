from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from google.oauth2 import id_token
from google.auth.transport import requests


def homepage(request):
    if request.session.get("id_token") is None :
        template = loader.get_template("webinterface/html/index.html")
        return HttpResponse(template.render())
    else:
        return HttpResponse("placeholder for logged in")

def about(request):
    template = loader.get_template("webinterface/html/aboutUs.html")
    return HttpResponse(template.render())

def loggedin(request):
    try:
        token = request.POST.get("idtoken")
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), "599761015615-krb4hqvd1m6nsl18r1am0glvcbdakb3d.apps.googleusercontent.com")
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        else:
            request.session['userid'] = idinfo['email']
            return redirect('/')
    except ValueError:
        pass
    

