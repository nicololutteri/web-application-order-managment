# Generated by Django 2.2.24 on 2021-07-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='id',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='credentials',
            table='credentials',
        ),
    ]
