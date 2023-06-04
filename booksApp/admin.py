from django.contrib import admin
from .models import *
from .customModelAdmin import book


class BookModelAdmin(book.BookDBModelAdmin):
    model = Book

admin.site.register(Book, BookModelAdmin)
