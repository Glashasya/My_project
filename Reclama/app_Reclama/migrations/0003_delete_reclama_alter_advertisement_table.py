# Generated by Django 4.2.4 on 2023-08-09 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_Reclama', '0002_reclama'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reclama',
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='reclama',
        ),
    ]
