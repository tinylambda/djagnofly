# Generated by Django 3.2.8 on 2021-10-24 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
        migrations.AlterModelTable(
            name='teacher',
            table='teachers',
        ),
    ]