from markdownx import fields as markdown_fields
from django import forms


class PostForm(forms.Form):
    body = markdown_fields.MarkdownxFormField()
