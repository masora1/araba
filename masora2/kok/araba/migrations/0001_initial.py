# Generated by Django 3.2.9 on 2022-01-25 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model', models.CharField(max_length=50)),
                ('Ulke', models.CharField(max_length=50)),
                ('Fiyat', models.IntegerField()),
                ('Km', models.IntegerField(null=True)),
                ('Tarih', models.DateField()),
            ],
        ),
    ]