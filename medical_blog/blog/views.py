from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Post, Tag
from .forms import CreatePostForm, CreateTagForm, UpdatePostForm, UpdateTagForm
from .mixins import ObjectDetailMixin


class PostsListView(ListView):
    template_name = 'blog/posts_page.html'
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = []
        for post in Post.objects.all()[::-1]:
            from bs4 import BeautifulSoup
            post.content = BeautifulSoup(post.content).get_text()
            posts.append(post)
        context['posts'] = posts
        return context


class PostBodyView(ObjectDetailMixin, View):
    model = Post
    template_name = 'blog/post_page.html'

    '''def get(self, request, *args, **kwargs):
        obj = Post.objects.get(post_slug__iexact=kwargs['post_slug'])
        return render(request, 'blog/post_page.html', context={'post': obj, 'admin_object': obj, 'detail': True})'''


def delete_post(request, post_slug):
    post = Post.objects.get(post_slug=post_slug)
    post.delete()
    return HttpResponseRedirect('/blog/',
                                render(request, 'blog/posts_page.html', context={'posts': Post.objects.all()}))


def delete_tag(request, tag_slug):
    tag = Tag.objects.get(tag_slug=tag_slug)
    tag.delete()
    return HttpResponseRedirect('/blog/tags/',
                                render(request, 'blog/tags_list.html', context={'tags': Tag.objects.all()}))


class SearchResultView(ListView):
    template_name = 'blog/search_result.html'

    def post(self, request):
        result = []

        if request.POST['search']:
            search_query = request.POST['search'].split()

            '''Старая версия поиска:
            for search_query in request.POST['search'].split():
                try:
                    tag_from_bd = Tag.objects.get(tag_slug__iexact=search_query)
                    tags_list.append(tag_from_bd)
                except ObjectDoesNotExist:
                    continue

            for tag in tags_list:
                for post in tag.posts.all():
                    if post not in posts_list:
                        posts_list.append(post)

            if tags_list:
                result = True

        return render(request, 'blog/search_result.html', context={'posts': posts_list, 'result': result})'''

            for query in search_query:
                db_query = Post.objects.filter(Q(post_title__icontains=query) | Q(body__icontains=query))
                if db_query:
                    for obj in db_query:
                        if obj not in result:
                            result.append(obj)
                try:
                    tag = Tag.objects.get(tag_slug__iexact=query)
                    for post in tag.posts.all():
                        if post not in result:
                            result.append(post)
                except ObjectDoesNotExist:
                    continue

            return render(request, 'blog/search_result.html', context={'posts': result})


class TagsListView(ListView):
    template_name = 'blog/tags_list.html'
    model = Tag
    context_object_name = 'tags'


class TagView(ObjectDetailMixin, View):
    model = Tag
    template_name = 'blog/tag.html'


class CreateFormView(LoginRequiredMixin, ListView):
    template_name = 'blog/create_form.html'
    model = Tag
    context_object_name = 'tags'

    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['post_form'] = CreatePostForm
        context['tag_form'] = CreateTagForm
        return context

    def post(self, request):
        save_success = False

        if 'post_title' in request.POST:
            post_form = CreatePostForm(request.POST, request.FILES or None)

            if post_form.is_valid():
                post = post_form.save()
                if request.POST['tags']:
                    for tag in request.POST['tags'].split():
                        try:
                            tag_from_bd = Tag.objects.get(tag_slug__iexact=tag)
                            post.tags.add(tag_from_bd)
                        except ObjectDoesNotExist:
                            tag_object = Tag(tag_title=tag, tag_slug=tag)
                            tag_object.save()
                            post.tags.add(tag_object)
                        finally:
                            post.save()
                save_success = True
            return render(request, 'blog/create_form.html', context={
                'post_form': post_form if not save_success else CreatePostForm,
                'tag_form': CreateTagForm, 'tags': Tag.objects.all(),
                'save_success': save_success})

        if 'tag_title' in request.POST:
            tag_form = CreateTagForm(request.POST)
            if tag_form.is_valid():
                tag_form.save()
                save_success = True
            return render(request, 'blog/create_form.html', context={
                'tag_form': tag_form if not save_success else CreateTagForm,
                'post_form': CreatePostForm, 'tags': Tag.objects.all(),
                'save_success': save_success})


class TagUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'blog/update.html'
    model = Tag
    form_class = UpdateTagForm
    slug_url_kwarg = 'tag_slug'
    slug_field = 'tag_slug'

    raise_exception = True


class PostUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'blog/update.html'
    model = Post
    form_class = UpdatePostForm
    slug_url_kwarg = 'post_slug'
    slug_field = 'post_slug'

    raise_exception = True
