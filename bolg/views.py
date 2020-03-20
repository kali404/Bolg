import re

import markdown
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.core.paginator import Paginator
from django.urls import reverse
from django.views import View
from bolg.models import *
import json


# Create your views here.

def get_top():
    catalog = Catalog.objects.filter(pcat=None, is_delete=False)
    Top_data = []
    for i in catalog:
        tab = {
            'id': i.id,
            'name': i.name,
            'lists': [i for i in Catalog.objects.filter(pcat=i.id)]
        }
        Top_data.append(tab)
    return Top_data


class IndexView(View):
    def get(self, request, ):
        page_num = request.GET.get('page_num')
        if page_num is None:
            page_num = 1
        articles = [i for i in Article.objects.filter(is_delete=False)]
        paginator = Paginator(articles, 10)
        pag_home = paginator.page(page_num)
        context = {
            'catalog': get_top(),
            'images': [image for image in LBTImg.objects.all()],
            'hots': [{'data': article, 'number': str(n + 1)} for n, article in
                     enumerate(Article.objects.filter(is_tag=True, is_delete=False))],
            'articles': pag_home,
            'pag_num': int(page_num),
            'cloud': [i for i in Tags.objects.filter()],
            'tops': Article.objects.filter(zan__gte=10, is_delete=False)  # 点赞超过10的

        }

        response = render_to_response('home.html', context)
        if request.COOKIES is None:

            response.set_cookie('like',[])
        return response


class ListViews(View):
    def get(self, request, list_id):
        page_num = request.GET.get('page_num')
        if page_num is None:
            page_num = '1'
        try:
            shangji = Catalog.objects.get(id=list_id).pcat.name + ' | '
        except:
            shangji = ''

        articles = Article.objects.filter(article_catalog=list_id)
        page = Paginator(articles, 15)
        page_home = page.page(page_num)
        context = {
            'catalog': get_top(),
            'fl': shangji + Catalog.objects.get(id=list_id).name,
            'page_home': page_home,
            'page_num': int(page_num),
            'list_id': list_id,
            'cloud': [i for i in Tags.objects.filter()],
            'tops': Article.objects.filter(zan__gte=10, is_delete=False).order_by('-zan')  # 点赞超过10的
        }
        return render(request, 'list.html', context)


class TagViews(View):
    def get(self, request, tag_id):
        page_num = request.GET.get('page_num')
        if page_num is None:
            page_num = '1'

        articles = []
        tag_all = TagZJ.objects.filter(tags_id=tag_id)
        for idzj in tag_all:
            for j in Article.objects.filter(id=idzj.article_id.id):
                articles.append(j)
        page = Paginator(articles, 10)
        page_home = page.page(page_num)
        context = {
            'catalog': get_top(),
            'fl': Tags.objects.get(id=tag_id).name,
            'page_home': page_home,
            'page_num': int(page_num),
            'list_id': tag_id,
            'cloud': [i for i in Tags.objects.filter()],
            'tops': Article.objects.filter(zan__gte=10, is_delete=False).order_by('-zan')  # 点赞超过10的
        }
        response = render(request, 'tags.html', context)

        return response


class ArticleView(View):
    def get(self, request, article_id):
        err = request.GET.get('err')

        # 分类
        type_one = Article.objects.get(id=article_id).article_catalog
        type_1 = type_one
        if type_one.pcat:
            type_2 = type_one.pcat
        else:
            type_2 = ''
        # 评论
        comments = Comment.objects.filter(article_id=article_id).order_by('create_time')
        comt_count = comments.count()
        comj = []
        for i in comments:
            comj.append({'data':i,'uid':str(int(str(i.user_id.id))%7)})

        articles = Article.objects.get(id=article_id, is_delete=False)
        articles.text = markdown.markdown(articles.text,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',])
        context = {
            'id':article_id,
            'catalog': get_top(),
            'type_1':type_1,
            'type_2':type_2,
            'article': articles,
            'couds_list': [i.tags_id for i in TagZJ.objects.filter(article_id=article_id)],
            'cloud': [i for i in Tags.objects.filter()],
            'tops': Article.objects.filter(zan__gte=10, is_delete=False).order_by('-zan'),
            'comt_count':comt_count,
            'comments':comj,
            'err':err,
        }

        response = render(request, 'info.html', context)
        if request.session.get('like') is None:
            request.session['like'] = []
        return response

    def post(self,request,article_id):
        # 接受
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        author = request.POST.get('author')
        # 验证
        if not all([email,comment,author]):
            return JsonResponse({"code":5,"errmsg":'三个选项都是必填的哦'})
        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return JsonResponse({"code":5,"errmsg":'参数email格式有误'})
        if UserPont.objects.filter(nicheng=author):
            if UserPont.objects.get(nicheng=author).email !=email:
                return JsonResponse({"code":5,"errmsg":'换个昵称,有人枪你的昵称,先来后到你改吧'})
        if UserPont.objects.filter(email=email):
            if UserPont.objects.get(email=email).nicheng != author:
                return JsonResponse({"code":5,"errmsg":'你邮箱被使用过了,邮箱和昵称不匹配,'})
        try:
            user = UserPont.objects.get(email=email,nicheng=author)
        except:
            user = UserPont.objects.create(
                username=email,
                email = email,
                nicheng=author,
                )

        Comment.objects.create(user_id=user,text=comment,article_id=Article.objects.get(id=article_id),)
        Article.objects.filter(id=article_id).update(pingl=Comment.objects.filter(article_id=article_id).count())

        return JsonResponse({
            "code":4,
            "errmsg":"评论成功,请手动刷新页面",
        })


class ZanViews(View):
    def get(self, request, article_id):
        like_list = request.session.get('like')
        if article_id in like_list:
            err = 1
            return JsonResponse({'code':err,'errmsg': '已经点过赞了'})
        else:
            zan = Article.objects.filter(id=article_id).update(zan=Article.objects.get(id=article_id).zan + 1,pingl=Comment.objects.filter(article_id=article_id).count())
            err = 4
            like_list.append(article_id)
            request.session['like']=like_list
            return  JsonResponse({
            'code': err,
            'errmsg': '点赞成功!'
        })

class AboutViews(View):
    def get(self,request):
        return render(request,'about.html')

class SearchViews(View):
    def get(self,request):
        search = request.GET.get('s')

        articles = Article.objects.filter(title__contains=search)
        context = {
            'catalog': get_top(),
            'fl': search,
            'page_home': articles,
            'cloud': [i for i in Tags.objects.filter()],
            'tops': Article.objects.filter(zan__gte=10, is_delete=False).order_by('-zan')  # 点赞超过10的
        }
        response = render(request, 'search.html', context)
        return response

def page_not_found(request, **kwargs):
    return render_to_response('404.html')

def page_error(request, **kwargs):
    return render_to_response('500.html')