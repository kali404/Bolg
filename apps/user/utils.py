import random

import markdown

from user.models import Catalog, UserPont, Article, TagZJ, Tags


def get_top():
    catalog = Catalog.objects.filter(pcat=None, is_delete=False)
    data = []
    for i in catalog:
        tab = {
            'id': i.id,
            'name': i.name,
            'lists': [i for i in Catalog.objects.filter(pcat=i.id)]
        }
        data.append(tab)
    return data


def get_myinfo(id):
    user_info = UserPont.objects.get(id=id, is_delete=False)
    return user_info


def get_article(catalog_id=None):
    if catalog_id is None:
        article = Article.objects.all()
    else:
        article = Article.objects.filter(article_catalog=catalog_id)
    articles = []
    for i in article:
        tags = []
        for j in TagZJ.objects.filter(article_id=i.id):
            tags.append(Tags.objects.get(id=j.tags_id.id))
        t = {
            'id': i.id,
            'title': i.title,
            'fenlei': Catalog.objects.get(id=i.article_catalog_id).name,
            'img': i.image.url,
            'brief': i.brief,
            'user_img': UserPont.objects.get(is_delete=False, id=i.article_user_id).img.url,
            'user_name': UserPont.objects.get(is_delete=False, id=i.article_user_id).nicheng,
            'create_time': i.create_time,
            'tags': tags,
            'pl': i.pingl,
            'zan': i.zan,
            'zhengwen': i.text,
        }
        articles.append(t)

    return articles


def get_article_index(catalog_id=None):
    if catalog_id is None:
        article = Article.objects.all()
    else:
        article = Article.objects.filter(article_catalog=catalog_id)
    articles = []
    for i in article:
        tags = []
        for j in TagZJ.objects.filter(article_id=i.id):
            tags.append(Tags.objects.get(id=j.tags_id.id))
        t = {
            'id': i.id,
            'title': i.title,
            'fenlei': Catalog.objects.get(id=i.article_catalog_id).name,
            'img': i.image.url,
            'brief': i.brief,
            'user_img': UserPont.objects.get(is_delete=False, id=i.article_user_id).img.url,
            'user_name': UserPont.objects.get(is_delete=False, id=i.article_user_id).nicheng,
            'create_time': i.create_time,
            'tags': tags,
            'pl': i.pingl,
            'zan': i.zan,
            'zhengwen': i.text,
        }
        articles.append(t)
        if len(article) >= 10:
            break
    return articles


def get_box_catalog(keyword):
    boxl = Catalog.objects.filter(splendid=True)
    tables = []
    for i in boxl:
        t = {
            'name': i.name,
            'id': i.id,
            'keyword': int(keyword),
        }
        tables.append(t)
    return tables


def get_box_img(keyword):
    box_imgs = []
    article_ids = Article.objects.filter(article_catalog=keyword)
    for i in article_ids:
        box_imgs.append(i)
        if len(box_imgs) >= 2:
            break
    return box_imgs


def get_box_article(keyword):
    box_article = []
    article_ids = Article.objects.filter(article_catalog=keyword)
    for i in article_ids:
        box_article.append(i)
        if len(box_article) >= 5:
            break
    return box_article


def get_header_artic():
    headers = []
    while 1:
        keyword = random.randint(0, Article.objects.all().count())
        try:
            article = Article.objects.get(id=keyword)
        except:
            continue
        else:
            if not headers:
                headers.append(article)
            elif headers[0] == article:
                continue
            else:
                headers.append(article)
        finally:
            if len(headers) >= 2:
                break

    return headers


def paihang():
    host = Article.objects.all().order_by('like_it')
    hosts = []
    for i, j in enumerate(host):
        t = {
            'id': i + 1,
            'data': j
        }
        hosts.append(t)
        if len(hosts) > 4:
            break
    return hosts


def zhiding():
    is_top = Article.objects.filter(is_tag=True, is_delete=False)
    tops = []
    for i in is_top:
        tops.append(i)
        if len(tops) >= 8:
            break
    return tops


def get_list(list_id):
    lists = Catalog.objects.get(id=list_id)
    return lists


def get_tags(tag):
    tag_list = Tags.objects.get(id=tag)
    return tag_list


def get_artice_couds(id):
    couds_list = []
    for i in TagZJ.objects.filter(article_id=id):
        couds_list.append(Tags.objects.get(id=i.tags_id_id).name)
    return couds_list


def get_clouds():
    clouds = []
    cloud = Tags.objects.all()
    for i in cloud:
        clouds.append(i)
        if len(clouds) > 15:
            break
    return clouds


def get_clouds_article(tag):
    article_lists = TagZJ.objects.filter(tags_id=tag)
    article_list = []
    for id in article_lists:
        article_list.append(id.article_id)
    print(article_list)
    artic = []
    for i in article_list:
        tags = []
        for j in TagZJ.objects.filter(article_id=i.id):
            tags.append(Tags.objects.get(id=j.tags_id.id))
        t = {
            'id': i.id,
            'title': i.title,
            'fenlei': Catalog.objects.get(id=i.article_catalog_id).name,
            'img': i.image.url,
            'brief': i.brief,
            'user_img': UserPont.objects.get(is_delete=False, id=i.article_user_id).img.url,
            'user_name': UserPont.objects.get(is_delete=False, id=i.article_user_id).nicheng,
            'create_time': i.create_time,
            'tags': tags,
        }
        artic.append(t)
        if len(artic) > 10:
            break
    return artic


def mianbao(article):
    tas = Article.objects.get(id=article)
    one = Catalog.objects.get(id=tas.article_catalog_id)

    return {'one': one.name, 'name': tas.title}


def get_article_text(id):
    text = Article.objects.get(id=id)
    t = {
        'id': text.id,
        'text': markdown.markdown(text.text),
        'zan': text.zan,
        'pingl': text.pingl,
        'create_time': text.create_time,
        'article_user': text.article_user,
        'article_catalog': text.article_catalog,

    }
    return t
