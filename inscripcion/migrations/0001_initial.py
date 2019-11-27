# Generated by Django 2.2.5 on 2019-11-26 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actividad', '0003_auto_20191126_1009'),
        ('evento', '0002_auto_20191126_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=150)),
                ('correo', models.EmailField(max_length=60)),
                ('DNI', models.CharField(max_length=8)),
                ('actividades', models.ManyToManyField(to='actividad.Actividad')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Evento')),
            ],
        ),
    ]