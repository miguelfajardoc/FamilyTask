# Generated by Django 3.1.4 on 2021-03-24 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familyTaskAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generaltask',
            name='programmed_date',
        ),
    ]
