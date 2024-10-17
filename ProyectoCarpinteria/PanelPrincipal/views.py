
# from carro.carro import Carro
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegistroUsuarioForm
from django.shortcuts import render, redirect
from django.contrib import messages


from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.


def home(request):
    # carro = Carro(request)
    return render(request, "PanelPrincipal/home.html")


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            # Redirige a la página principal después del registro
            return redirect('Home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'formulario/formulario.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                # Redirige a la página principal después del inicio de sesión
                return redirect('Home')
            else:
                messages.error(request, "Verifica los datos...")
                # Redirige a la página principal después del inicio de sesión
        else:
            messages.error(request, "Verifica los datos...")
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect("Home")


def enviar_correo(request):
    subject = 'Asunto del correo'
    message = 'UNA ORDEN DE CHULETA PARA LA CALLA 32'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['jhonbttm1998@gmail.com',]

    send_mail(subject, message, email_from, recipient_list)

    return HttpResponse('Correo enviado!')
