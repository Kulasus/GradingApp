# Generated by Django 3.0.1 on 2019-12-29 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.TextField(default='password'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.TextField(default='password'),
        ),
    ]