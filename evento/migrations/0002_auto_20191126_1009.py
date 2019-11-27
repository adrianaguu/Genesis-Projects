# Generated by Django 2.2.5 on 2019-11-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje_descuento', models.FloatField(max_length=4)),
                ('limite_uso', models.IntegerField()),
                ('codigo', models.CharField(max_length=16)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='eventotipo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='evento',
            name='descuentos',
            field=models.ManyToManyField(null=True, to='evento.Descuento'),
        ),
    ]
