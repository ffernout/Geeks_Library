from datetime import datetime
from django.http import HttpResponse
# Create your views here.


def about_me(request):
    if request.method == 'GET':
        return HttpResponse("<h1>About Me</h1><p>This is the about me page.</p>")

def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse("<h1>About My Pets</h1><p>This is the About My Pets page.</p>")

def date_time(request):
    current_time = datetime.now()
    return HttpResponse(f"<h1>Current Time</h1><p>Current time is: {current_time}</p>")

