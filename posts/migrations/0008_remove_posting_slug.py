# Generated by Django 3.1.1 on 2020-10-02 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20201002_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='slug',
        ),
    ]