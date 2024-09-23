# Generated by Django 4.2.1 on 2023-05-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='operating_system',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='computer',
            name='IP_address',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='computer',
            name='MAC_address',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='computer',
            name='computer_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='computer',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='computer',
            name='users_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
