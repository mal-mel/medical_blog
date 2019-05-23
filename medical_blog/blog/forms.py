from django import forms
from .models import Post, Tag
from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget


class CreatePostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['post_title', 'content', 'image']

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px;', 'required': 'true'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['post_slug'].lower()

        if Post.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Слаг должен быть уникальным и состоять только из букв, цифр, подчеркиваний или дефисов.')
        return new_slug


class CreateTagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['tag_title', 'tag_slug']

        widgets = {
            'tag_title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px;', 'required': 'true'}),
            'tag_slug': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px;', 'required': 'true'})
        }


class UpdatePostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['post_title', 'post_slug', 'content', 'image', 'tags']

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px;', 'required': 'true'}),
            'post_slug': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px;', 'required': 'true'}),
            'tags': forms.SelectMultiple(attrs={'class': 'browser-default custom-select', 'style': 'width: 500px;'})
        }


class UpdateTagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['tag_title', 'tag_slug']

        widgets = {
            'tag_title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px;', 'required': 'true'}),
            'tag_slug': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px;', 'required': 'true'})
        }
