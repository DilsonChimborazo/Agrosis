# Generated by Django 5.1.1 on 2024-12-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herramientas', '0002_alter_herramientas_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herramientas',
            name='estado',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('En reparación', 'En reparación'), ('Prestado', 'Prestado')], max_length=50, null=True),
        ),
    ]
