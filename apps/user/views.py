from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from user.models import Catalog, LBTImg, Wailian
from user.utils import *


class IndexView(View):
    def get(self, request):
        keyword = request.GET.get('keyword')
#        if keyword is None:
#            keyword = Catalog.objects.filter(splendid=True)[0].id
        context = {
            'user': get_myinfo(1),
            'catalog': get_top(),
            'articles': get_article_index(),
#            'tables': get_box_catalog(keyword),
#            'box_img': get_box_img(keyword),
#            'box_artic': get_box_article(keyword),
            'header_artic': get_header_artic,
            'hosts': paihang(),
            'tops': zhiding(),
            'images': LBTImg.objects.all(),
            'cloud': get_clouds(),
            'wailian': Wailian.objects.all(),
        }
        return render(request, 'index.html', context)


class ListView(View):
    def get(self, request, list_id, page_num):
        pcat_id = Catalog.objects.get(id=list_id).pcat
        id_list = []
        data = []
        data += get_article(list_id)
        if pcat_id is None:
            a = Catalog.objects.filter(pcat=list_id)
            for i in a:
                id_list.append(i.id)
            for id in id_list:
                data += get_article(id)
        if page_num is None:
            page_num = 1
        # paginator = Paginator(data, 10)
        # page_skus = paginator.page(page_num)
        # total_page = paginator.num_pages
        paginator = Paginator(data, 10)  # 查询出来的对象经过序列化后的字典的列表
        page_home = paginator.page(page_num)  # 分页数
        # context = {'page_article': page_home, 'page_num': int(page_num)}

        context = {
            'id':list_id,
            'fl': Catalog.objects.get(id=list_id).name,
            'user': get_myinfo(1),
            'catalog': get_top(),
            'lists': get_list(list_id),
            'hosts': paihang(),
            'tops': zhiding(),
            'cloud': get_clouds(),
            'page_home': page_home,
            'page_num': int(page_num),
            'wailian':Wailian.objects.all(),


        }
        return render(request, 'list.html', context)


class TagsView(View):
    def get(self, request, tag_id):

        context = {
            'fl': Tags.objects.get(id=tag_id).name,
            'catalog': get_top(),
            'page_home': get_clouds_article(tag_id),
            'lists': get_list(tag_id),
            'hosts': paihang(),
            'tops': zhiding(),
            'cloud': get_clouds(),
        }
        return render(request, 'list.html', context)


class ArticleView(View):
    def get(self, request, article_id):
        context = {
            'user': get_myinfo(1),
            'catalog': get_top(),
            'mianbao': mianbao(article_id),
            'article': get_article_text(article_id),
            'couds_list': get_artice_couds(article_id),
            'cloud': get_clouds(),
            'tops': zhiding(),
        }
        return render(request, 'info.html', context)
