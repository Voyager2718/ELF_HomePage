# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_id', models.IntegerField()),
                ('severity', models.IntegerField()),
                ('status', models.IntegerField()),
                ('reported_by', models.IntegerField()),
                ('hide_to_public', models.BooleanField(default=False)),
                ('information', models.TextField(max_length=65535)),
                ('description', models.TextField(max_length=65535)),
            ],
        ),
        migrations.CreateModel(
            name='BugStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_status_id', models.IntegerField()),
                ('bug_status_name', models.CharField(max_length=32)),
                ('bug_status_description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='BugSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('support_end_day', models.DateField()),
                ('product_name', models.TextField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocked', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('user_role', models.CharField(default='Users', max_length=32)),
            ],
        ),
    ]
