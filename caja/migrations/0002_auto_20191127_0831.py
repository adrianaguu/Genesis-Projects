# Generated by Django 2.2.5 on 2019-11-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salida',
            name='concepto',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='salida',
            name='numero_documento',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
