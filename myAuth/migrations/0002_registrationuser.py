# Generated by Django 4.1 on 2023-12-26 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAuth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('confirmPassword', models.CharField(max_length=255)),
            ],
        ),
    ]
