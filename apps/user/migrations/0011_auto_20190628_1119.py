# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-06-28 03:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20190628_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 11, 19, 44, 315050), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 11, 19, 44, 315079), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 11, 19, 44, 318288), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 11, 19, 44, 317682), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='liek',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 11, 19, 44, 319643), verbose_name='点赞时间'),
        ),
        migrations.AlterField(
            model_name='tagzj',
            name='article_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Article', verbose_name='文章id'),
        ),
    ]