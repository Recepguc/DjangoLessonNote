from django.shortcuts import render
from django.http import HttpResponse


def database(request):
    return HttpResponse("Welcome")
