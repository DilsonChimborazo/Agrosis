# Generated by Django 5.1.1 on 2024-12-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='rol',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]