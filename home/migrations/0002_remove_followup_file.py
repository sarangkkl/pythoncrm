# Generated by Django 3.2.4 on 2021-09-21 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followup',
            name='file',
        ),
    ]
