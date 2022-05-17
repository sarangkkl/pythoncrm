# Generated by Django 3.2.7 on 2021-09-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('address_1', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('email_1', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_2', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=14, null=True)),
                ('recuring_time', models.IntegerField()),
                ('period', models.IntegerField()),
                ('pin_code', models.CharField(blank=True, max_length=14, null=True)),
                ('documents', models.FileField(upload_to='customer/documnets')),
            ],
        ),
    ]
