from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from google.oauth2 import id_token
from google.auth.transport import requests
from django.views.decorators.csrf import csrf_exempt
from webinterface.models import Song
import json
def homepage(request):
    print(request.session.get('user'))
    if request.session.get("user") is None :
        template = loader.get_template("webinterface/html/index.html")
        return HttpResponse(template.render())
    else:
        template = loader.get_template("webinterface/html/homePageLogin.html")
        return HttpResponse(template.render())

def about(request):
    template = loader.get_template("webinterface/html/aboutUs.html")
    return HttpResponse(template.render())

@csrf_exempt
def loggedin(request):
    json_data = json.loads(request.body.decode("utf-8"))
    token = json_data["id"]
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), "599761015615-krb4hqvd1m6nsl18r1am0glvcbdakb3d.apps.googleusercontent.com")
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            print("invalid")
            return redirect('/') 
        else:
            request.session['user'] = idinfo['email']
            return redirect('/')
    except ValueError:
        print("error")
        return redirect('/')

def addsong(request):
    if request.session.get("user") is not None :
        song = Song(song_name="123", userid = request.session.get("user"))
        song.save()
    return redirect('/')
    

