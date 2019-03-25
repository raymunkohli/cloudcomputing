from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

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
    request.session["idtokens"] = request.POST.get("idtoken")
    return redirect('/')

