# Generated by Django 5.1.3 on 2024-11-22 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_customer_person_address_person_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
