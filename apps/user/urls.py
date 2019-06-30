from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^list/(?P<list_id>\d+)/(?P<page_num>\d+)/$', views.ListView.as_view()),
    url(r'^tags/(?P<tag_id>\d+)/$', views.TagsView.as_view()),
    url(r'^article/(?P<article_id>\d+)/$', views.ArticleView.as_view()),
]
