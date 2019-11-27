from django.shortcuts import render
from django.utils import timezone
from .models import Evento,EventoTipo
from actividad.models import Actividad
from .forms import InscripcionForm


"""Método que da todos los registros de la Tabla Evento Tipo a la interfaz index"""
def type_event_list(request):
    tipos = EventoTipo.objects.all()
    return render(request, 'evento/index.html', {'tipos': tipos})

def event_list(request, pk):
    tipo = EventoTipo.objects.get(pk=pk)
    eventos =Evento.objects.filter(tipo=tipo)
    return render(request, 'evento/tipoEvento.html', {'eventos': eventos,'tipo':tipo})

def event(request, pk):
    evento = Evento.objects.get(pk=pk)
    actividades = Actividad.objects.filter(evento=evento)
    return render(request, 'evento/evento.html', {'evento': evento,'actividades':actividades})

def inscripcion(request, pk):
    evento = Evento.objects.get(pk=pk)
    if request.method == "POST":
        form = InscripcionForm(evento,request.POST)
        print (form['actividades'].value())
        actividades = Actividad.objects.filter(pk__in=form['actividades'].value())
        sum=0
        for actividad in actividades.all():
            sum=sum+actividad.costo_inscripcion
        if form.is_valid():
            #form.cleaned_data['actividades'] = actividades
            inscripcion = form.save(commit=False)
            inscripcion.evento = evento
            inscripcion.monto=sum
            inscripcion.save()
            inscripcion.actividades.set(actividades)
            inscripcion.save()

            return render(request,'evento/index.html',{})
    else:
        form = InscripcionForm(evento=evento)
    return render(request, 'evento/inscripcion.html', {'form': form,'evento':evento})
