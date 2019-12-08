from django.contrib import admin
from .models import ControlAsistencia, ControlMaterial, ControlCaja, ControlInscritos, Certificado
from django_object_actions import DjangoObjectActions
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from inscripcion.models import Inscripcion
from caja.models import Ingreso, Salida


#admin.site.register(ControlAsistencia)

#Código de caso de uso relacionado: C11-03
@admin.register(ControlMaterial)
class ReportAdminMaterial(DjangoObjectActions, admin.ModelAdmin):

    def generate_pdf(self, request, obj):
        html_string = render_to_string('reportes/materiales_pdf.html', {'obj': obj})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response

        return response

    generate_pdf.label = 'Generer Reporte'
    generate_pdf.short_description = 'Haga click para generar el reporte de los materiales'

    change_actions = ('generate_pdf',)


#Código de caso de uso relacionado: C11-02
@admin.register(ControlAsistencia)
class ReportAdminAsistencia(DjangoObjectActions, admin.ModelAdmin):

    def generate_pdf(self, request, obj):
        html_string = render_to_string('reportes/asistencia_pdf.html', {'obj': obj})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response

        return response

    generate_pdf.label = 'Generer Reporte'
    generate_pdf.short_description = 'Haga click para generar el reporte de los asistentes'

    change_actions = ('generate_pdf',)

#Código de caso de uso relacionado: C11-05
@admin.register(ControlCaja)
class ReportAdminCaja(DjangoObjectActions, admin.ModelAdmin):

    def generate_pdf(self, request, obj):
        monto = 0
        ingresos = Ingreso.objects.filter(evento=obj.evento)
        salidas = Salida.objects.filter(evento=obj.evento)
        for ingreso in ingresos:
            monto = monto + ingreso.cantidad
        for salida in salidas:
            monto = monto - salida.cantidad
        html_string = render_to_string('reportes/caja_pdf.html', {'obj': obj,'ingresos':ingresos,'salidas':salidas,'monto':monto})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response

        return response

    generate_pdf.label = 'Generer Reporte'
    generate_pdf.short_description = 'Haga click para generar el reporte de la caja   '

    change_actions = ('generate_pdf',)

#Código de caso de uso relacionado: C11-01
@admin.register(ControlInscritos)
class ReportAdminInscritos(DjangoObjectActions, admin.ModelAdmin):

    def generate_pdf(self, request, obj):
        inscripciones = Inscripcion.objects.filter(evento=obj.evento)
        html_string = render_to_string('reportes/inscritos_pdf.html', {'obj': obj,'inscripciones':inscripciones})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response

        return response

    generate_pdf.label = 'Generer Reporte'
    generate_pdf.short_description = 'Haga click para generar el reporte de los Inscritos'

    change_actions = ('generate_pdf',)


#Código de caso de uso relacionado: C11-04
@admin.register(Certificado)
class ReportAdminInscritos(DjangoObjectActions, admin.ModelAdmin):

    def generate_pdf(self, request, obj):
        asistentes = ControlAsistencia.objects.get(evento=obj.evento)
        html_string = render_to_string('reportes/certificados_pdf.html', {'obj': obj,'control':asistentes})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response

        return response

    generate_pdf.label = 'Generar Certificados'
    generate_pdf.short_description = 'Haga click para generar los certificados'

    change_actions = ('generate_pdf',)