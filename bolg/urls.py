#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 上午11:16
# @Author  : Aries
# @File    : urls.py
# @Software: PyCharm
# @Email   : dewujie64@gmail.com

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view()),
    url(r'^list/(?P<list_id>\d+)',views.ListViews.as_view()),
    url(r'^tags/(?P<tag_id>\d+)',views.TagViews.as_view()),
    url(r'^article/(?P<article_id>\d+)',views.ArticleView.as_view()),
    url(r'^zan/(?P<article_id>\d+)',views.ZanViews.as_view()),
    url(r'^search',views.SearchViews.as_view()),
    url(r'^about',views.AboutViews.as_view()),
]