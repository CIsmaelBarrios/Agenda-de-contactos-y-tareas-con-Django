# Generated by Django 5.0.1 on 2024-02-25 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='note',
            new_name='notes',
        ),
    ]
