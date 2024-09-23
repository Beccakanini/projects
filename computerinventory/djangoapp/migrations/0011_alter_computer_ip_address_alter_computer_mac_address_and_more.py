# Generated by Django 4.2.1 on 2023-06-30 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0010_update_alter_computerhistory_computer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='IP_address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='MAC_address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='computer_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='users_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='email_address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='confirm_password',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='email_address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='computer_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
