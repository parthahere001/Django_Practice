from django.urls import path
from django.http import HttpResponse
from .import views
urlpatterns = [path('',views.index,name='index'),
path('add/', views.add,name='add'),
path('add/addrecord/', views.addrecord, name='addrecord'),
]
