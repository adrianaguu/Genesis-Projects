# Generated by Django 2.2.5 on 2019-11-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0002_auto_20191127_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlasistencia',
            name='asistentes',
            field=models.ManyToManyField(blank=True, to='inscripcion.Inscripcion'),
        ),
    ]