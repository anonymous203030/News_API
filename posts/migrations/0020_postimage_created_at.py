# Generated by Django 3.1.1 on 2020-10-04 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20201004_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]