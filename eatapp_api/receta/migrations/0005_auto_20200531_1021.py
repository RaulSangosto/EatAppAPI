# Generated by Django 3.0.4 on 2020-05-31 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0004_auto_20200531_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='categorias',
            field=models.ManyToManyField(blank=True, related_name='receta', to='receta.Categoria'),
        ),
    ]
