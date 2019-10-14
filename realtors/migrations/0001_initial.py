# Generated by Django 2.2.6 on 2019-10-14 00:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]