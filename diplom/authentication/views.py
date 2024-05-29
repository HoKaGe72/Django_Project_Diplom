from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import CustomAuthenticationForm
from .models import AuthUser

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            request.session.set_expiry(settings.SESSION_EXPIRE_SECONDS)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})
