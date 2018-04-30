from django.contrib import admin

# Register your models here.
from app.models import Moment, Comment, Contact, Account

admin.site.register(Moment)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Account)
