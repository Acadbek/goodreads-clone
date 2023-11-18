from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from goodreads.views import landingPage
from django.conf.urls.static import static


urlpatterns = [
    path('', landingPage, name='landingPage'),
    path('users/', include('user.urls')),
    path('books/', include('book.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
