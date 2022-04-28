# Generated by Django 2.2.10 on 2022-04-28 14:24

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=20, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
    ]
