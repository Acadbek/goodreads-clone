from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View
from user.forms import UserCreateForm, UserLoginForm


class RegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html', {'form': UserCreateForm()})

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('user:login')
        else:
            return render(request, 'users/register.html', {'form': create_form})


class LoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('landingPage')

        else:
            return render(request, 'users/login.html', {"form": form})
