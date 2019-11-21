# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-22 17:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EverNoteCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oauth_token', models.CharField(max_length=100)),
                ('oauth_token_secret', models.CharField(max_length=100)),
                ('oauth_verifier', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
