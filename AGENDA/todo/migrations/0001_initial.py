# Generated by Django 5.0.1 on 2024-02-24 02:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('desciption', models.TextField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('estimated_end', models.DateField(blank=True, null=True)),
                ('priority', models.IntegerField(default=3)),
            ],
        ),
    ]