from random import choice
from django.http import HttpResponse
from django.shortcuts import render


from .models import Poll



def index(request):
    choice = ""
    for poll in Poll.objects.all():
        choice = choice + " " + poll.name
    return HttpResponse(choice) # Test
