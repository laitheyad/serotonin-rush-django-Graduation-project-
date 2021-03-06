# Generated by Django 3.1.5 on 2021-02-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SerotoninRush', '0002_auto_20210207_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('fats', models.FloatField()),
                ('protein', models.FloatField()),
                ('carbohydrate', models.FloatField()),
                ('recipe', models.TextField()),
            ],
        ),
    ]
