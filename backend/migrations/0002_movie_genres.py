# Generated by Django 3.2 on 2021-04-27 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='backend.Genre'),
        ),
    ]
