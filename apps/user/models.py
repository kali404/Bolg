import datetime

from mdeditor.fields import MDTextField
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserPont(AbstractUser):
    nicheng = models.CharField(max_length=20, verbose_name='昵称')
    zhiye = models.CharField(max_length=20, verbose_name='职业')
    xianju = models.CharField(max_length=20, verbose_name='现居')
    qqimage = models.ImageField(verbose_name='qq二维码')
    weixin = models.ImageField(verbose_name='微信二维码')
    img = models.ImageField(verbose_name='用户头像')
    is_delete = models.BooleanField(verbose_name='是否删除此用户', default=False)


class Catalog(models.Model):
    """博客分类"""
    name = models.CharField('分类', max_length=128)
    pcat = models.ForeignKey('self', null=True, blank=True, related_name='sj', verbose_name='上级分类')
    splendid = models.BooleanField(verbose_name='是否将此类在首页展示', default=False)
    shuoming = models.CharField(max_length=128, verbose_name='分类说明', default='可能，你觉得自己没有足够得优秀，但我始终相信你仍然在努力坚持着!')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    def __str__(self):
        return self.name

    class Meta:
        # ordering = ['-created_time']
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name


class Tags(models.Model):
    """文章标签"""
    name = models.CharField(max_length=128, verbose_name='标签名字')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = verbose_name


class Article(models.Model):
    """文章表"""
    title = models.CharField(max_length=128, verbose_name='标题')
    brief = models.CharField(max_length=200, verbose_name='简介')
    text = MDTextField(verbose_name='正文')
    image = models.ImageField(verbose_name='预览图')
    article_user = models.ForeignKey(UserPont, verbose_name='作者')
    article_catalog = models.ForeignKey(Catalog, verbose_name='文章类型')
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.datetime.now())
    update_time = models.DateTimeField(verbose_name='更新时间', default=datetime.datetime.now())
    is_tag = models.BooleanField(verbose_name='是否推荐&置顶', default=False)
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)
    like_it = models.IntegerField(verbose_name='访问量', default=0)
    zan = models.IntegerField(verbose_name='点赞数', default=0)
    pingl = models.IntegerField(verbose_name='评论量', default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class TagZJ(models.Model):
    """标签中间"""
    article_id = models.ForeignKey(Article, verbose_name='文章id')
    tags_id = models.ForeignKey(Tags, verbose_name='标签id')

    def __str__(self):
        return str(self.article_id)

    class Meta:
        verbose_name = '标签中间表'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    """文章评论"""
    article_id = models.ForeignKey(Article, verbose_name='文章id')
    text = MDTextField(verbose_name='评论正文', max_length=256)
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.datetime.now())
    user_id = models.ForeignKey(UserPont, verbose_name='用户')
    parent_id = models.ForeignKey('self', verbose_name='上级评论')

    def __str__(self):
        return self.article_id

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name


class Attention(models.Model):
    """用户与用户"""
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.datetime.now())
    user_id = models.ForeignKey(UserPont, verbose_name='主用户')
    target_user_id = models.IntegerField(verbose_name='从用户')
    relation = models.IntegerField(default=0, verbose_name='状态')

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = '用户关注'
        verbose_name_plural = verbose_name


class LBTImg(models.Model):
    """首页轮播图"""
    image = models.ImageField(verbose_name='轮播图')
    user_id = models.ForeignKey(UserPont, verbose_name='用户')
    title = models.CharField(max_length=20, verbose_name='描述', default='站长很忙没写描述啊,有意见来打我呀')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '首页轮播图'
        verbose_name_plural = verbose_name


class Liek(models.Model):
    """点赞表"""
    article_id = models.ForeignKey(Article, verbose_name='文章id')
    create_time = models.DateTimeField(verbose_name='点赞时间', default=datetime.datetime.now())
    user_id = models.ForeignKey(UserPont, verbose_name='用户')
    relation = models.IntegerField(verbose_name='对文章状态')

    def __str__(self):
        return '为{}操作'.format(self.article_id)

    class Meta:
        verbose_name = '点赞'
        verbose_name_plural = verbose_name


class Wailian(models.Model):
    hear = models.CharField(verbose_name='连接地址不需要http://', max_length=128)
    name = models.CharField(verbose_name='外联名字', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '为您推荐'
        verbose_name_plural = verbose_name
