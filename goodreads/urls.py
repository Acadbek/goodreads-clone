from django.contrib import admin
from django.urls import path

from goodreads.views import landingPage

urlpatterns = [
    path('', landingPage, name='landingPage'),
    path('admin/', admin.site.urls),
]
