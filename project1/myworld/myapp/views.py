from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Myapp

def index(request):
   mymembers=Myapp.objects.all().values()
   output=" "
   for x in mymembers:
           output+=x["firstname"]
   return HttpResponse(output)

# Create your views here.
