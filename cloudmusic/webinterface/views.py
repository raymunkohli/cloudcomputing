from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def homepage(request):
    if request.session.get("login") is None :
        template = loader.get_template("webinterface/html/index.html")
        return HttpResponse(template.render())
    else:
        return HttpResponse("placeholder for logged in")

def about(request):
    template = loader.get_template("webinterface/html/aboutUs.html")
    return HttpResponse(template.render())

