from django.shortcuts import render
from frontend import *

def ind(request):
    return render(request, 'index.html')
