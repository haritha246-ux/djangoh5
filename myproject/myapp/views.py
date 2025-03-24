from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
    return HttpResponse("Hi This is home page")
def firstpage(request):
    return HttpResponse("This is First page")
def secondpage(request):
    return HttpResponse("This is Second page")
def html_page(request):
    template = loader.get_template('std.html')
    return HttpResponse(template.render())

