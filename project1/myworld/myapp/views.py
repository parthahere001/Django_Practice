from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Myapp

def index(request):
   mymembers=Myapp.objects.all().values()
   template=loader.get_template('index.html')
   context={
            'mymembers':mymembers,
           }
   return HttpResponse(template.render(context,request))
def add(request):
   template=loader.get_template('add.html')
   return HttpResponse (template.render({},request))
def addrecord(request):
   x=request.POST['first']
   y=request.POST['last']
   member=Myapp(firstname=x,lastname=y)
   member.save()
   return HttpResponseRedirect(reverse('index'))
def delete(request, id):
  member = Myapp.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))
# Create your views here.
