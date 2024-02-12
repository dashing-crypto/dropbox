from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class CustomLoginView(LoginView):
    template_name = 'login.html'
    #success_url = reverse_lazy('sig')


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to your login page after logout


