# Generated by Django 4.2.1 on 2023-05-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0008_remove_computer_operating_system_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_name', models.CharField(blank=True, max_length=30)),
                ('IP_address', models.CharField(blank=True, max_length=30)),
                ('MAC_address', models.CharField(blank=True, max_length=30)),
                ('users_name', models.CharField(blank=True, max_length=30)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('export_csv', models.BooleanField(default=False)),
                ('purchase_date', models.DateTimeField(blank=True, null=True, verbose_name='purchase_date(mm/dd/yyyy)')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
