from django import forms
from .models import BlogEntry


class BlogEntryForm(forms.Modelform):
    class Meta:
        model = BlogEntry
        fields = ['title', 'content']