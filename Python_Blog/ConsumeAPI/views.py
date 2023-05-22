
from django.shortcuts import render
from django.views import generic
from django.conf import settings 
import requests

# Create your views here.

def getuser(request):
         
    res = requests.get(settings.apiurl)
    books = res.json()
    return render(request,'api/books.html',{"books": books})