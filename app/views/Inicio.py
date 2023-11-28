#from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def inicio(request):
    return render(request, 'Index.html')