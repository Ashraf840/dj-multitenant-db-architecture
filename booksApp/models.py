from django.db import models

class Book(models.Model):
    # authors = models.ManyToManyField(Author)
    content = models.TextField()

    class Meta():
        verbose_name_plural = 'Book'
        app_label = 'booksApp'
