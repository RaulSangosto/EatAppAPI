# Generated by Django 3.0.4 on 2020-04-24 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0002_auto_20200416_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='ingredientes',
        ),
        migrations.CreateModel(
            name='Instruccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(blank=True, max_length=100, null=True)),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receta.Ingrediente')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receta.Receta')),
            ],
        ),
    ]
