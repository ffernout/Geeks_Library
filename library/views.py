from django.shortcuts import render
from datetime import datetime
# Create your views here.


def about_me(request):
    return render(request, 'library/about_me.html')

def about_my_pets(request):
    return render(request, 'library/about_my_pets.html')

def date_time(request):
    current_time = datetime.now()
    return render(request, 'library/date_time.html',
                  {'current_time': current_time})

