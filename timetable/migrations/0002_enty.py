# Generated by Django 3.1.3 on 2020-11-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_C', models.CharField(max_length=1000)),
                ('name_I', models.CharField(max_length=70)),
                ('Romm_number', models.CharField(max_length=10)),
                ('Thu', models.CharField(max_length=10)),
                ('Ca', models.CharField(max_length=10)),
            ],
        ),
    ]
