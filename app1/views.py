"""
My first django view
"""

from django.http import HttpResponse
from django.shortcuts import render
# TODO - refer
# https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#render


def home(request):
    return HttpResponse('Hello, World!')


def welcome(request):
    return render(request, "app1/welcome.html")


def another(request):
    return render(request, "app1/dynamic.html", {"name": "Ratna"})