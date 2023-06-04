from django.db import models


class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()

    class Meta():
        verbose_name_plural = 'Author'
        app_label = 'authorApp'