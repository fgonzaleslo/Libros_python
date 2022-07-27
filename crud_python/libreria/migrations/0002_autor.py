# Generated by Django 3.2.8 on 2022-06-27 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('dni', models.IntegerField(max_length=8, verbose_name='DNI')),
                ('direccion', models.TextField(null=True, verbose_name='Direccion')),
                ('libro_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='libreria.libro')),
            ],
        ),
    ]