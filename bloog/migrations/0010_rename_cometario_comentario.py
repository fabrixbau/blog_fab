# Generated by Django 5.0.2 on 2024-02-23 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloog', '0009_alter_cometario_autor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cometario',
            new_name='Comentario',
        ),
    ]
