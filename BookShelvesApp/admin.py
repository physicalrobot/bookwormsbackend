from django.contrib import admin

# Register your models here.
from .models import BookShelf


class BookShelfAdmin(admin.ModelAdmin):
    readonly_fields=('BookShelfId',)

admin.site.register(BookShelf, BookShelfAdmin),