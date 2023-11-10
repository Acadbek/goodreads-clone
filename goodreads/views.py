from django.http import HttpResponse


def landingPage(request):
    return HttpResponse(f"hello: {request.META['HTTP_USER_AGENT']}")