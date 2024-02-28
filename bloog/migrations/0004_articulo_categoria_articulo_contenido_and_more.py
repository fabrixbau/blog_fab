# Generated by Django 5.0.2 on 2024-02-21 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloog', '0003_alter_articulo_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.CharField(choices=[('general', 'General'), ('diseño web', 'Diseño web'), ('programación', 'Programación'), ('ux/ix', 'UX/IX')], default='general', max_length=50),
        ),
        migrations.AddField(
            model_name='articulo',
            name='contenido',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='articulo',
            name='duracion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='articulo',
            name='fecha_registro',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='articulos'),
        ),
    ]