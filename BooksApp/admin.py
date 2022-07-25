from django.contrib import admin

from .models import Book
from .models import Genre


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('BookId',)


class GenreAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Book, BookAdmin),
admin.site.register(Genre, GenreAdmin),

# Register your models here.
