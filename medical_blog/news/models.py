from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from ckeditor.fields import RichTextField
from time import time


def gen_slug(s):
    return slugify(s, allow_unicode=True) + '-' + str(int(time()))


class News(models.Model):

    title = models.CharField(max_length=150, db_index=True)
    content = RichTextField(db_index=True)
    source = models.URLField(max_length=150, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('news_page_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.post_slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_delete_url(self):
        return reverse('news_delete_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('news_update_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
