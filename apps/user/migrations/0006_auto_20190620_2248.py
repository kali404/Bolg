# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-20 14:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190620_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 20, 22, 48, 16, 146658), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=mdeditor.fields.MDTextField(verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 20, 22, 48, 16, 146684), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 20, 22, 48, 16, 149091), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 20, 22, 48, 16, 148261), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=mdeditor.fields.MDTextField(max_length=256, verbose_name='评论正文'),
        ),
        migrations.AlterField(
            model_name='liek',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 20, 22, 48, 16, 150386), verbose_name='点赞时间'),
        ),
    ]
