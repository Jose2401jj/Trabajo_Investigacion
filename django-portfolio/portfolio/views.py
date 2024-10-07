from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .models import Experiencia,Educacion

@login_required
def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

class CustomLoginView(LoginView):
    template_name = 'login.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Este usuario ya está registrado.')
                return render(request, 'register.html', {'form': form})

            form.save()
            messages.success(request, 'Tu cuenta ha sido creada. Puedes iniciar sesión ahora.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def experiencia_view(request):
    experiencias = Experiencia.objects.all()
    return render(request, 'experiencia.html', {'experiencias': experiencias})

def educacion_view(request):
    educaciones = Educacion.objects.all() 
    return render(request, 'educacion.html', {'Educaciones': educaciones})