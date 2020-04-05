from django import forms
from markdownx import fields as markdown_fields


class PostForm(forms.Form):
    body = markdown_fields.MarkdownxFormField()
