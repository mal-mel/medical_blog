from django.views.generic import ListView
from django.shortcuts import render
from .models import News


class NewsView(ListView):
    template_name = 'news/news_page.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'news/news_page.html', context={'news': News.objects.get(title__iexact=kwargs['title'])})

