# Generated by Django 3.0 on 2019-12-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('temperature', models.FloatField()),
                ('rainfall', models.FloatField()),
                ('barometricPressure', models.FloatField()),
                ('humidity', models.IntegerField()),
                ('windSpeed', models.IntegerField()),
                ('windDirection', models.CharField(max_length=5)),
            ],
        ),
    ]
