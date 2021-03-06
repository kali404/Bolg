# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-19 13:08
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190619_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='brief',
            field=models.CharField(max_length=200, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 21, 8, 4, 866588), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 21, 8, 4, 866615), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 21, 8, 4, 869060), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='主用户'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 21, 8, 4, 868522), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='liek',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 21, 8, 4, 870275), verbose_name='点赞时间'),
        ),
    ]
