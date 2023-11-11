from django.http import HttpResponse
from django.shortcuts import render


def landingPage(request):
    return render(request, 'landing.html')