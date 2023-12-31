from django.urls import path
from user.views import RegisterView, LoginView, ProfileView, LogoutView, UpdateProfileView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', UpdateProfileView.as_view(), name='profile-edit')
]
