from django.views import View
from django.shortcuts import redirect, render
from user.forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


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
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('books:list')
        else:
            return render(request, 'users/login.html', {"form": form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html', {'user': request.user})


class LogoutView(View):
    def get(self, request):
        messages.info(request, 'You have been logged out')
        logout(request)
        return redirect('landingPage')
