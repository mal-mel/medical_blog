from django import forms
from .models import Post, Tag
from django.core.exceptions import ValidationError


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_title', 'body', 'image']

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px;', 'required': 'true'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 300px; width: 750px; resize: none;', 'required': 'true'}),
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

    class Meta:
        model = Post
        fields = ['post_title', 'post_slug', 'body', 'image', 'tags']

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px;', 'required': 'true'}),
            'post_slug': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px;', 'required': 'true'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 300px; width: 750px; resize: none;', 'required': 'true'}),
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
