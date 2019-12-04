# Generated by Django 3.0 on 2019-12-04 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('archive_file', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('PE', 'Pending'), ('RU', 'Running'), ('CO', 'Complete'), ('FA', 'Failure')], default='PE', max_length=2)),
            ],
        ),
    ]