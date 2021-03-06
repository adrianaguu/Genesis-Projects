# Generated by Django 2.2.5 on 2019-11-27 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inscripcion', '0004_inscripcion_dia_hora_asistencia'),
        ('evento', '0007_auto_20191126_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlAsistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Evento')),
                ('participantes', models.ManyToManyField(to='inscripcion.Inscripcion')),
            ],
        ),
    ]
