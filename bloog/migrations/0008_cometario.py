# Generated by Django 5.0.2 on 2024-02-23 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloog', '0007_alter_articulo_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cometario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(default='')),
                ('autor', models.CharField(max_length=255)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bloog.articulo')),
            ],
        ),
    ]
