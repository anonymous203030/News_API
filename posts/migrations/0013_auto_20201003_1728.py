# Generated by Django 3.1.1 on 2020-10-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20201003_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='posting',
            name='choices',
        ),
        migrations.AddField(
            model_name='posting',
            name='categories',
            field=models.ManyToManyField(to='posts.Category'),
        ),
    ]