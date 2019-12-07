from django.contrib import admin
from .models import ControlAsistencia, ControlMaterial, ControlCaja, ControlInscritos, Certificado
from django_object_actions import DjangoObjectActions
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


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

#Código de caso de uso relacionado: C11-01
@admin.register(ControlInscritos)
class ReportAdminInscritos(DjangoObjectActions, admin.ModelAdmin):

    def generate_pdf(self, request, obj):
        html_string = render_to_string('reportes/Inscritos_pdf.html', {'obj': obj})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response

        return response

    generate_pdf.label = 'Generer Reporte'
    generate_pdf.short_description = 'Haga click para generar el reporte de los Inscritos   '

    change_actions = ('generate_pdf',)

#Código de caso de uso relacionado: C11-01
@admin.register(ControlInscritos)
class ReportAdminInscritos(DjangoObjectActions, admin.ModelAdmin):

    def generate_pdf(self, request, obj):
        html_string = render_to_string('reportes/Inscritos_pdf.html', {'obj': obj})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response

        return response

    generate_pdf.label = 'Generer Reporte'
    generate_pdf.short_description = 'Haga click para generar el reporte de los Inscritos   '

    change_actions = ('generate_pdf',)