import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def date_time(request):
    time=datetime.datetime.now()
    s=('<h1> the time in the server is : ' + str(time) + '</h1>')
    return HttpResponse(s)
