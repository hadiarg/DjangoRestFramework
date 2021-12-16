# Generated by Django 3.2.7 on 2021-12-15 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('store_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='', upload_to='static/media/')),
                ('fav', models.BooleanField(default=False)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]