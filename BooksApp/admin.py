from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    readonly_fields=('BookId',)

admin.site.register(Book, BookAdmin)

# Register your models here.
