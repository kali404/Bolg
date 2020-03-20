import re

from django.contrib import admin
from bolg.models import *
from utils.image_to_qiniu import markdown_to_img, img_to_qiniu


admin.site.site_header = '夜风随笔'
admin.site.site_title = '夜风随笔后台'
admin.site.index_title = '欢迎使用夜风随笔博客管理'



class AriticleAdmin(admin.ModelAdmin):

    # 可编辑字段

    fields = ['title','text','image','article_catalog','is_tag']
    # 列表显示字段
    list_display = ['title','brief','article_catalog','is_tag']
    search_fields = ('title',)
    # 复写save方法,将简介自动保存文章的前50个字
    def save_model(self, request, obj, form, change):
        obj.brief = obj.text[:100]
        obj.text = markdown_to_img(obj.text)
        if change:
            obj.image = img_to_qiniu(str(obj.image))
        super().save_model(request, obj, form, change)



class TagZJAdmin(admin.ModelAdmin):
    pass


class CatalogAdmin(admin.ModelAdmin):


    fields = ['name','pcat','shuoming','is_delete']
    list_display = ['name','pcat','shuoming']

admin.site.register(UserPont)
admin.site.register(Article,AriticleAdmin,)
admin.site.register(Catalog,CatalogAdmin)
admin.site.register(Comment)
admin.site.register(Tags)
admin.site.register(TagZJ, TagZJAdmin)
admin.site.register(Attention)
admin.site.register(LBTImg)
admin.site.register(Wailian)
