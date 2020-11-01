# Generated by Django 3.1.1 on 2020-10-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0007_auto_20201003_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='user',
        ),
        migrations.AddField(
            model_name='subscription',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]