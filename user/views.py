from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from user.forms import UserCreateForm


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        ctx = {'form': create_form}

        return render(request, 'users/register.html', ctx)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('user:login')
        else:
            ctx = {
                'form': create_form
            }
            return render(request, 'users/register.html', ctx)


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')
