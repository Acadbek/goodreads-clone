from django.shortcuts import render


def landingPage(request):
    # print('COOKIES', request.COOKIES['csrftoken'])
    render(request, 'landing.html')
