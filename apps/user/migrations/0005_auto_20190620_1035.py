# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-20 02:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190620_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='shuoming',
            field=models.CharField(default='可能，你觉得自己没有足够得优秀，但我始终相信你仍然在努力坚持着!', max_length=128, verbose_name='分类说明'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 20, 10, 35, 10, 947207), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_tag',
            field=models.BooleanField(default=False, verbose_name='是否推荐&置顶'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 20, 10, 35, 10, 947242), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 20, 10, 35, 10, 949441), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 20, 10, 35, 10, 948706), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='liek',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 20, 10, 35, 10, 950614), verbose_name='点赞时间'),
        ),
    ]
