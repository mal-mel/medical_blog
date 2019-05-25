from django.views.generic import ListView, UpdateView
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News
from .forms import UpdateNewsForm


class NewsView(ListView):
    template_name = 'news/news_page.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'news/news_page.html', context={'news': News.objects.get(slug__iexact=kwargs['slug']),
                                                               'detail': True,
                                                               'admin_object': News.objects.get(slug__iexact=kwargs['slug'])})


def delete_news(request, slug):

    if request.user.is_authenticated and request.user.is_superuser:
        news = News.objects.get(slug=slug)
        news.delete()
        return HttpResponseRedirect('/',
                                    render(request, 'main.html', context={'news': News.objects.all()}))
    return HttpResponseForbidden()


class UpdateNews(LoginRequiredMixin, UpdateView):
    template_name = 'blog/update.html'
    model = News
    form_class = UpdateNewsForm
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    raise_exception = True
