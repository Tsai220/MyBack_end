# Generated by Django 4.2.5 on 2023-10-01 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usrInfo', '0003_rename_user_id_userinfo_id_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='id_user',
            new_name='user_id',
        ),
    ]
