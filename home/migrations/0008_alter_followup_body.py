# Generated by Django 3.2.7 on 2021-11-23 16:16

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210923_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]