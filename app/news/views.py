from comments.forms import PostCommentForm
from comments.models import PostComment
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.views.generic import View, ListView, UpdateView
from markdownx.utils import markdownify

from .forms import PostForm
from .models import Post


class PostsListView(ListView):
    template_name = 'news/posts_list.html'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-timestamp')
        for post in posts:
            post.body = markdownify(post.body)
        return render(request, self.template_name, {'posts': posts, })


class PostDetailView(View):
    template_name = 'news/post_details.html'
    form_class = PostCommentForm

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs.get('pk'))
        comments = PostComment.objects.filter(post=post.pk).order_by('-timestamp')
        post.body = markdownify(post.body)
        return render(request, self.template_name, {'post': post, 'form': self.form_class(), 'comments': comments, })

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        post = Post.objects.get(pk=kwargs.get('pk'))
        if form.is_valid():
            post_comment = PostComment.objects.create(
                post=post,
                creator=request.user,
                body=form.cleaned_data['body'],
            )
            html_message = render_to_string('email/commented_post.html', {
                'domain': get_current_site(request).domain,
                'pk': post.pk,
                'commentator': post_comment.creator.email,
            })
            post.creator.email_user('PLANEKS News', strip_tags(html_message), html_message=html_message)
            return redirect('posts:details', post.pk)
        return render(request, self.template_name, {'post': post, 'form': form, })


class PostCreateView(View):
    template_name = 'news/post_create.html'
    form_class = PostForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class(), })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = Post.objects.create(
                creator=request.user,
                body=form.cleaned_data['body'],
            )
            return redirect('posts:main')
        return render(request, self.template_name, {'form': form, })


class PostEditView(UpdateView):
    template_name = 'news/post_edit.html'
    model = Post
    fields = [
        'body',
    ]
    success_url = '/'
