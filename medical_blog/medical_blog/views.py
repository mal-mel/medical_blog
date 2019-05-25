from django.views.generic import ListView
from django.shortcuts import redirect

from news_parser import parser
from blog.models import Post
from news.models import News


class MainPageView(ListView):
    template_name = 'main.html'
    model = parser(News)
    ordering = ['-id']
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[::-1][:6] if len(Post.objects.all()[::-1][:6]) >= 6 \
            else Post.objects.all()[::-1]
        return context


def update_news_list(request):
    parser(News)
    return redirect('/')
