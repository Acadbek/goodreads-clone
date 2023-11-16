from django.contrib import admin
from django.urls import path, include
from goodreads.views import landingPage

urlpatterns = [
    path('', landingPage, name='landingPage'),
    path('users/', include('user.urls')),
    path('books/', include('book.urls')),
    path('admin/', admin.site.urls),
]
