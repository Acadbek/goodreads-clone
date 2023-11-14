from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        
        user.set_password(password)
        user.save()
        
        return redirect('user:login')


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')
