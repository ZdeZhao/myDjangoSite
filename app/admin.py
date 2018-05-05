from django.contrib import admin

# Register your models here.
from app.models import Moment, Comment, Contact, Account


class MomentAdmin(admin.ModelAdmin):
    search_fields = ('content',)

    class Meta:
        models = Moment

admin.site.register(Moment, MomentAdmin)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Account)
