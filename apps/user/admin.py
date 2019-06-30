from django.contrib import admin
from . import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'visiting', 'created_time', 'modifyed_time']


class A(admin.ModelAdmin):
    pass


admin.site.register(models.Catalog)
admin.site.register(models.Tags)
admin.site.register(models.Article)
admin.site.register(models.TagZJ)
admin.site.register(models.Attention)
admin.site.register(models.LBTImg)
admin.site.register(models.Liek)
admin.site.register(models.Comment, A)
admin.site.register(models.Wailian, A)
admin.site.register(models.UserPont, A)
