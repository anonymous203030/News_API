# Generated by Django 3.1.1 on 2020-10-04 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_postimage_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.ImageField(blank=True, upload_to='post_image/'),
        ),
    ]
