# Generated by Django 3.1.1 on 2020-10-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20201003_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='images',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
