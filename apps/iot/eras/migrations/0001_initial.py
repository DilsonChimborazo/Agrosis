# Generated by Django 5.1.1 on 2024-12-06 03:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fk_id_lote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lote.lote')),
            ],
        ),
    ]
