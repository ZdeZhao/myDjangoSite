from django.contrib import admin

# Register your models here.
from app.models import Moment, Comment, Contact, Account, Moments


class MomentAdmin(admin.ModelAdmin):
    list_display = ('pk', "content", "user_name", 'kind',)
    fieldsets = (
        ("消息内容", {
            'fields': ('content', 'kind')
        }),
        ("用户信息", {
            'fields': ('user_name',)
        }),
    )
    search_fields = ('content', 'user_name',)

admin.site.register(Moment, MomentAdmin)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Account)
