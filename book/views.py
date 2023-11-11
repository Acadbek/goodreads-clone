from django.shortcuts import render


def landingPage(request):
    render(request, 'landing.html')
