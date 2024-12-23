# Generated by Django 5.1.3 on 2024-11-21 12:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_name', models.CharField(max_length=255)),
                ('C_address', models.CharField(max_length=255, validators=[django.core.validators.MaxLengthValidator(255), django.core.validators.MinLengthValidator(10)])),
                ('C_contact', models.BigIntegerField(unique=True)),
                ('C_email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator])),
                ('C_age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(70), django.core.validators.MinValueValidator(18)])),
                ('C_image', models.ImageField(upload_to='Image/customer_image')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.MaxLengthValidator(255), django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AddField(
            model_name='person',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(70), django.core.validators.MinValueValidator(18)]),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator]),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='Image/User_image'),
        ),
    ]
