# Generated by Django 2.2.5 on 2019-11-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0003_auto_20191127_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcion',
            name='dia_hora_asistencia',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
