from email.mime import base
from django.shortcuts import render

# Create your views here.

def frontpage(request):
    return render(request, 'frontpage.html')
    