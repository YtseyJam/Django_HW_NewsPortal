from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from newsportal.models import Author
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


