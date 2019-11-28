from django.shortcuts import render
from django.utils import timezone
from .models import Evento,EventoTipo,Descuento
from actividad.models import Actividad
from reportes.models import ControlAsistencia, ControlMaterial
from .forms import InscripcionForm, ControlAsistenciaForm, ControlMaterialForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect



"""Método que da todos los registros de la Tabla Evento Tipo a la interfaz index"""
#Códigos de casos de uso relacionado: C13,C14,C15
def type_event_list(request):
    tipos = EventoTipo.objects.all()
    return render(request, 'evento/index.html', {'tipos': tipos})


"""Método que da todos los registros de la Tabla Evento de Tipo Evento con id=pk a la interfaz tipoEvento"""
#Códigos de casos de uso relacionado: C13,C14,C15
def event_list(request, pk):
    tipo = get_object_or_404(EventoTipo, pk=pk)
    eventos =Evento.objects.filter(tipo=tipo)
    return render(request, 'evento/tipoEvento.html', {'eventos': eventos,'tipo':tipo})

#Códigos de casos de uso relacionado: C13,C14,C15
def event(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    actividades = Actividad.objects.filter(evento=evento)
    return render(request, 'evento/evento.html', {'evento': evento,'actividades':actividades})


#Códigos de casos de uso relacionado: C13,C14,C15
def control_asistencia(request,pk):
    evento = get_object_or_404(Evento, pk=pk)
    control = ControlAsistencia.objects.get(evento=evento)
    if request.method == "POST":
        form = ControlAsistenciaForm(evento, request.POST, instance=control)
        if form.is_valid():#Si la informacion ingresada por el usuario es válida
            control = form.save()
            return redirect('event', pk=evento.pk)
    else:
        form = ControlAsistenciaForm(evento=evento,instance=control)
    return render(request, 'evento/control_asistencia.html', {'form': form,'evento':evento})

#Códigos de casos de uso relacionado: C13,C14,C15
def control_materiales(request,pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    evento = get_object_or_404(Evento, pk=actividad.evento.pk)
    control = get_object_or_404(ControlMaterial, actividad=actividad)
    if request.method == "POST":
        form = ControlMaterialForm(actividad, request.POST, instance=control)
        if form.is_valid():#Si la informacion ingresada por el usuario es válida
            control = form.save()
            return redirect('event', pk=evento.pk)
    else:
        form = ControlMaterialForm(actividad=actividad,instance=control)
    return render(request, 'evento/control_materiales.html', {'form': form,'actividad':actividad,'evento':evento})

#Códigos de casos de uso relacionado: C13,C14,C15
def inscripcion(request, pk):
    evento = Evento.objects.get(pk=pk)
    actividadess = Actividad.objects.filter(evento=evento)
    if request.method == "POST":
        form = InscripcionForm(evento,request.POST)
        print (form['codigo_descuento'].value())
        actividades = Actividad.objects.filter(pk__in=form['actividades'].value())
        sum=0#variable donde se acumula el costo de inscripcion de todas las actividades seleleccionadas por el usuario
        
        if form.is_valid():#Si la informacion ingresada por el usuario es válida
            for actividad in actividades.all():
                sum=sum+actividad.costo_inscripcion#se calcula el monto de la inscripcion
                
                
            inscripcion = form.save(commit=False)
            inscripcion.evento = evento
            if(form['codigo_descuento']):#Si el usuario coloco codigo de descuento
                if(Descuento.objects.filter(codigo=form['codigo_descuento'].value()).exists()):#Si el codigo de descuento existe
                    descuento=Descuento.objects.get(codigo=form['codigo_descuento'].value())
                    porcentaje_descuento = descuento.porcentaje_descuento
                    sum=sum-(sum*porcentaje_descuento/100)#aplicar descuento

            inscripcion.monto=sum
            inscripcion.save()
            inscripcion.actividades.set(actividades)
            inscripcion.save()

            return render(request,'evento/index.html',{'mensaje':'Su inscripción fue exitosa'})
    else:
        form = InscripcionForm(evento=evento)
    return render(request, 'evento/inscripcion.html', {'form': form,'evento':evento,'actividades':actividadess})
