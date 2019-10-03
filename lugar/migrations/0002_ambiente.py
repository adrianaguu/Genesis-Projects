# Generated by Django 2.2.5 on 2019-10-03 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=200, unique=True)),
                ('ubicación', models.CharField(max_length=500)),
                ('capacidad', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(max_length=10)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lugar.Lugar')),
            ],
        ),
    ]
