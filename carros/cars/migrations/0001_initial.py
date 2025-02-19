# Generated by Django 5.1.6 on 2025-02-17 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=20)),
                ('factory_year', models.IntegerField()),
                ('model_yaer', models.IntegerField()),
                ('value', models.FloatField()),
            ],
        ),
    ]
