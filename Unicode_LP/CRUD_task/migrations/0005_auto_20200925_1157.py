# Generated by Django 3.1.1 on 2020-09-25 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_task', '0004_auto_20200923_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mail_model',
            old_name='seen',
            new_name='seenby_recv',
        ),
        migrations.AddField(
            model_name='mail_model',
            name='seenby_sender',
            field=models.BooleanField(default=False),
        ),
    ]
