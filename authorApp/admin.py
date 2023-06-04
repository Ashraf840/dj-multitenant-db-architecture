from django.contrib import admin
from .models import *
from .customModelAdmin import author

# Specialize the multi-db admin objects for use with specific models.
class AuthorModelAdmin(author.AuthorDBModelAdmin):
    model = Author


admin.site.register(Author, AuthorModelAdmin)

