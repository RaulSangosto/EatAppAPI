# Generated by Django 3.0.4 on 2020-06-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0007_auto_20200609_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='dieta',
            field=models.CharField(choices=[('o', 'Omnivora'), ('v', 'Vegetariana'), ('n', 'Vegana')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]