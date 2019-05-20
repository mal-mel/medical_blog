from django.db import models
from django.shortcuts import reverse


class News(models.Model):

    title = models.CharField(max_length=150, db_index=True)
    body = models.TextField(db_index=True)
    source = models.URLField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('news_page_url', kwargs={'title': self.title})

    def __str__(self):
        return self.title
