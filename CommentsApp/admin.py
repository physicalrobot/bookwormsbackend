from django.contrib import admin

# Register your models here.
from .models import Comment


# class CommentAdmin(admin.ModelAdmin):
#     readonly_fields = ('account_id',)


admin.site.register(Comment)
