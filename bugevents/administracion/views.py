from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from administracion import *
from configuracion.models import *
from configuracion.forms import *


'''
Caso de uso relacionado: BE01 Iniciar Sesion
Clase de diseno relacionada: CD65 ControlAutenticacion
'''
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/admin')

        messages.info(request, 'Autenticación fallida.')

    context = {}
    return render(request, 'administracion/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def dashboard(request):
    eventos = Evento.objects.all().order_by('fecha_inicio')
    context = {'eventos': eventos}
    return render(request, 'administracion/dashboard.html', context)


def recursos(request):
    recursos = {"ambientes", "materiales", "ponentes"}
    context = {"recursos": sorted(recursos)}
    return render(request, 'administracion/recursos.html', context)


'''
Clase de diseno relacionada: CD38 ControlMaterial
'''
def materialIndex(request):
    materiales = Material.objects.all()
    context = {'materiales': materiales, 'obj_name_plural': 'materiales'}
    return render(request, 'administracion/materialIndex.html', context)


'''
Clase de diseno relacionada: CD23 ControlAmbiente
'''
def ambienteIndex(request):
    ambientes = Ambiente.objects.all()
    context = {'ambientes': ambientes, 'obj_name_plural': 'ambientes'}
    return render(request, 'administracion/ambienteIndex.html', context)


'''
Clase de diseno relacionada: CD74 ControlPonente
'''
def ponenteIndex(request):
    ponentes = Ponente.objects.all()
    context = {'ponentes': ponentes, 'obj_name_plural': 'ponentes'}
    return render(request, 'administracion/ponenteIndex.html', context)
