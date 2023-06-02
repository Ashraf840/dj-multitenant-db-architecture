from django.contrib import admin
from .models import *
from .customModelAdmin import author
from .customModelAdmin import book

# Specialize the multi-db admin objects for use with specific models.
class AuthorModelAdmin(author.AuthorDBModelAdmin):
    model = Author

class BookModelAdmin(book.BookDBModelAdmin):
    model = Book

admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Book, BookModelAdmin)
