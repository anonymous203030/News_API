# Generated by Django 3.1.1 on 2020-10-01 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200930_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_image/'),
        ),
    ]
