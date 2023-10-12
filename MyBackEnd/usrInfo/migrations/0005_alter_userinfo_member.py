# Generated by Django 4.2.5 on 2023-10-01 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usrInfo', '0004_rename_id_user_userinfo_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='member',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MinValueValidator(3)]),
        ),
    ]
