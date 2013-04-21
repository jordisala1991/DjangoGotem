from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'gotem/index.html', context)