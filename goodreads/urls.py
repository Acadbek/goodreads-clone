from django.contrib import admin
from django.urls import path, include
from goodreads.views import landingPage

urlpatterns = [
    path('', landingPage, name='landingPage'),
    path('users/', include('user.urls'), name='users'),
    path('admin/', admin.site.urls),
]
