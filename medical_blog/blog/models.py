from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from ckeditor.fields import RichTextField

from time import time


def gen_slug(s):
    return slugify(s, allow_unicode=True) + '-' + str(int(time()))


class Post(models.Model):

    post_title = models.CharField(max_length=100, db_index=True)
    post_slug = models.SlugField(max_length=100, unique=True, blank=True)
    content = RichTextField(blank=True, db_index=True)
    image = models.ImageField(null=True, blank=True, upload_to='%Y/%m/%d/')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_body_url', kwargs={'post_slug': self.post_slug})

    def get_update_url(self):
        return reverse('update_post_url', kwargs={'post_slug': self.post_slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'post_slug': self.post_slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.post_slug = gen_slug(self.post_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.post_title


class Tag(models.Model):

    tag_title = models.CharField(max_length=50)
    tag_slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_url', kwargs={'tag_slug': self.tag_slug})

    def get_update_url(self):
        return reverse('update_tag_url', kwargs={'tag_slug': self.tag_slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'tag_slug': self.tag_slug})

    def __str__(self):
        return self.tag_title

