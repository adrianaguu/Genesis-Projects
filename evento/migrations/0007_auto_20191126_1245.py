# Generated by Django 2.2.5 on 2019-11-26 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0006_remove_eventotipo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='descuentos',
            field=models.ManyToManyField(blank=True, related_name='eventos', to='evento.Descuento'),
        ),
    ]
