from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *
from .forms import * 


'''
Clase de diseno relacionada: CD84 ControlEvento
'''
def eventoShow(request, pk):
    evento = Evento.objects.get(id=pk)
    actividades = evento.actividad_set.all()
    for i, a in enumerate(actividades):
        turnos = a.turno_set.all()
        a.turno_count = turnos.count()

    context = {'evento': evento, 'actividades': actividades}

    return render(request, 'configuracion/eventoShow.html', context)


'''
Caso de uso relacionado: BE04 Crear Evento
Diagrama de secuencia relacionado: BE04 Crear Evento
Clase de diseno relacionada: CD84 ControlEvento
'''
def eventoCreate(request):
    form = EventoForm()
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'model_form.html', context)


'''
Caso de uso relacionado: BE05 Modificar Evento
Diagrama de secuencia relacionado: BE05 Modificar Evento
Clase de diseno relacionada: CD84 ControlEvento
'''
def eventoUpdate(request, pk):
    evento = Evento.objects.get(id=pk)
    form = EventoForm(instance=evento)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'object': evento}
    return render(request, 'model_form.html', context)


'''
Clase de diseno relacionada: CD84 ControlEvento
'''
def eventoDelete(request, pk):
    evento = Evento.objects.get(id=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('dashboard')

    context = {'object': evento}
    return render(request, 'configuracion/delete.html', context)


'''
Caso de uso relacionado: BE13 Anadir Material
Diagrama de secuencia relacionado: BE13 Anadir Material
Clase de diseno relacionada: CD38 ControlMaterial
'''
class MaterialCreate(CreateView):
    model = Material
    fields = '__all__'
    template_name = 'model_form.html'
    success_url = reverse_lazy('materialIndex')


'''
Caso de uso relacionado: BE14 Modificar Material
Diagrama de secuencia relacionado: BE14 Modificar Material
Clase de diseno relacionada: CD38 ControlMaterial
'''
class MaterialUpdate(UpdateView):
    model = Material
    fields = '__all__'
    template_name = 'model_form.html'
    success_url = reverse_lazy('materialIndex')


'''
Clase de diseno relacionada: CD38 ControlMaterial
'''
class MaterialDelete(DeleteView):
    model = Material
    success_url = reverse_lazy('materialIndex')
    template_name = 'configuracion/delete.html'


'''
Caso de uso relacionado: BE07 Crear Ambiente
Diagrama de secuencia relacionado: BE07 Crear Ambiente
Clase de diseno relacionada: CD23 ControlAmbiente
'''
class AmbienteCreate(CreateView):
    model = Ambiente
    fields = '__all__'
    template_name = 'model_form.html'
    success_url = reverse_lazy('ambienteIndex')


'''
Caso de uso relacionado: BE08 Modificar Ambiente
Diagrama de secuencia relacionado: BE08 Modificar Ambiente
Clase de diseno relacionada: CD23 ControlAmbiente
'''
class AmbienteUpdate(UpdateView):
    model = Ambiente
    fields = '__all__'
    template_name = 'model_form.html'
    success_url = reverse_lazy('ambienteIndex')


'''
Clase de diseno relacionada: CD23 ControlAmbiente
'''
class AmbienteDelete(DeleteView):
    model = Ambiente
    success_url = reverse_lazy('ambienteIndex')
    template_name = 'configuracion/delete.html'


'''
Clase de diseno relacionada: CD74 ControlPonente
'''
class PonenteCreate(CreateView):
    model = Ponente
    fields = '__all__'
    template_name = 'model_form.html'
    success_url = reverse_lazy('ponenteIndex')


'''
Clase de diseno relacionada: CD74 ControlPonente
'''
class PonenteUpdate(UpdateView):
    model = Ponente
    fields = '__all__'
    template_name = 'model_form.html'
    success_url = reverse_lazy('ponenteIndex')


'''
Clase de diseno relacionada: CD74 ControlPonente
'''
class PonenteDelete(DeleteView):
    model = Ponente
    success_url = reverse_lazy('ponenteIndex')
    template_name = 'configuracion/delete.html'
