# Generated by Django 3.0.4 on 2020-04-28 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='invitacion',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='permiso_escanear',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='permiso_staff',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='permiso_tickets',
        ),
    ]
