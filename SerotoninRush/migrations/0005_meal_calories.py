# Generated by Django 3.1.5 on 2021-02-10 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SerotoninRush', '0004_userreaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='calories',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
