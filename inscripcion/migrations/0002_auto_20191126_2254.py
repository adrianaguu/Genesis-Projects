# Generated by Django 2.2.5 on 2019-11-26 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscripcion',
            old_name='apellidos',
            new_name='apellido',
        ),
    ]
