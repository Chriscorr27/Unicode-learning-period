# Generated by Django 3.1.1 on 2020-09-23 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CRUD_task', '0003_auto_20200828_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('chat', models.TextField()),
                ('date_Of_Msg', models.DateTimeField(auto_now_add=True)),
                ('seen', models.BooleanField(default=False)),
                ('reciver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reciver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Chat_model',
        ),
    ]
