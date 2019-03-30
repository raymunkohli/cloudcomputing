from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.shortcuts import redirect
from google.oauth2 import id_token
from google.auth.transport import requests
from django.views.decorators.csrf import csrf_exempt
from webinterface.models import Song
from django.db.models import *
import webinterface.models
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

@csrf_exempt
def addsong(request):
    if request.session.get("user") is not None :
        song = Song(song_name=request.POST.get("name"), 
                    userid = request.session.get("user"),
                    link = request.POST.get("url"),
                    language = request.POST.get("lang"),
                    year = request.POST.get("year"),
                    genre = request.POST.get("genre"),
                    artist = request.POST.get("artist"),
                    album = request.POST.get("album"))
        song.save()
    return redirect('/')

def viewlibrary(request):
    songs = Song.objects.filter(
        userid__exact= request.session.get('user'),
    )
    return render_to_response("webinterface/html/library.html",{"songs":songs} )

@csrf_exempt
def updatelibrary(request):
    json_data = json.loads(request.body.decode("utf-8"))
    print(json.dumps(json_data))
    songs = Song.objects.filter(
        song_name__contains= json_data["name"], 
        year__contains= json_data["year"],
        genre__contains= json_data["genre"],
        artist__contains= json_data["artist"],
        language__contains= json_data["lang"],
        userid__exact= request.session.get('user'),
    )
    print(songs)
    return render_to_response("webinterface/html/updatelibrary.html",{"songs":songs} )

def logout(request):
    del request.session['user']
    request.session.modified = True
    return redirect("/")

def remove(request):
    songs = Song.objects.filter(
        idsong__exact = request.GET.get("name"),
        userid__exact = request.session.get('user')
    )
    if songs.count() == 1:
        songs.delete()
    return redirect("/viewlibrary")

@csrf_exempt
def update(request):
    print(request.session.get('user'))
    songs = Song.objects.filter(
        idsong__exact = request.POST.get("id"),
        userid__exact = request.session.get('user')
    ).update(
        song_name = request.POST.get("name"),
        link = request.POST.get("url"),
        language = request.POST.get("lang"),
        year = request.POST.get("year"),
        genre = request.POST.get("genre"),
        artist = request.POST.get("artist"),
        album = request.POST.get("album")
        )
    return redirect("/viewlibrary")

