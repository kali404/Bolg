# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-06-30 09:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20190628_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wailian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hear', models.CharField(max_length=128, verbose_name='连接地址不需要http://')),
                ('name', models.CharField(max_length=128, verbose_name='外联名字')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 30, 17, 1, 8, 513942), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 30, 17, 1, 8, 514047), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='attention',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 30, 17, 1, 8, 517165), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 30, 17, 1, 8, 516507), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='liek',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 30, 17, 1, 8, 518444), verbose_name='点赞时间'),
        ),
    ]
