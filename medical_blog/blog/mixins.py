from django.shortcuts import get_object_or_404, render
from .models import Tag, Post


class ObjectDetailMixin:
    model = None
    template_name = None

    def get(self, request, **kwargs):
        slug = kwargs['post_slug'] if self.model is Post else kwargs['tag_slug']

        obj = get_object_or_404(self.model, tag_slug__iexact=slug) if self.model is Tag else get_object_or_404(self.model, post_slug__iexact=slug)

        if obj.__class__ is Post:
            from django.utils.safestring import mark_safe
            obj.content = mark_safe(obj.content)

        return render(request, self.template_name, context={
            self.model.__name__.lower(): obj,
            'admin_object': obj,
            'detail': True,
            'tag_posts': obj.posts.all()[::-1] if obj.__class__ is Tag else None
        }
                      )
