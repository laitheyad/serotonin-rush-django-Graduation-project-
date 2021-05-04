# Generated by Django 3.1.5 on 2021-02-07 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SerotoninRush', '0003_meal'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('reaction', models.IntegerField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SerotoninRush.meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SerotoninRush.user')),
            ],
        ),
    ]
