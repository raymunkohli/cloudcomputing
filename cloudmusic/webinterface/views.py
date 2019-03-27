from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from google.oauth2 import id_token
from google.auth.transport import requests
from django.views.decorators.csrf import csrf_exempt

def homepage(request):
    print(request.session.get('user'))
    if request.session.get("user") is None :
        template = loader.get_template("webinterface/html/index.html")
        return HttpResponse(template.render())
    else:
        return HttpResponse("placeholder for logged in")

def about(request):
    template = loader.get_template("webinterface/html/aboutUs.html")
    return HttpResponse(template.render())

@csrf_exempt
def loggedin(request):
    for a in request.POST:
        print("asdf"+a)
    token = request.POST.get("id_token")
    print("token-: " + str(token))
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), "599761015615-krb4hqvd1m6nsl18r1am0glvcbdakb3d.apps.googleusercontent.com")
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            print("invalid")
            return redirect('/12313') 
        else:
            request.session['user'] = idinfo['email']
            return redirect('/')
    except ValueError:
        print("brokenwiajdoai")
        return redirect('/aaaaaaaa')
    

