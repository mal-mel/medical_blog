from django import forms
from .models import News
from ckeditor.widgets import CKEditorWidget


class UpdateNewsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = ['title', 'content']
