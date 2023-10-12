# Generated by Django 4.2.5 on 2023-10-03 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usrInfo', '0005_alter_userinfo_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
