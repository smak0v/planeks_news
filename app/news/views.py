from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView
from markdownx.utils import markdownify

from .forms import PostForm
from .models import Post


class PostsListView(ListView):
    template_name = 'news/posts_list.html'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-timespan')
        for post in posts:
            post.body = markdownify(post.body)
        return render(request, self.template_name, {'posts': posts, })


class PostDetailView(View):
    template_name = 'news/post_details.html'

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs.get('pk'))
        post.body = markdownify(post.body)
        return render(request, self.template_name, {'post': post, })


class PostCreateView(View):
    template_name = 'news/post_create.html'
    form_class = PostForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, })

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = Post.objects.create(
                creator=request.user,
                body=form.cleaned_data['body'],
            )
            return redirect('posts:main')
        return render(request, self.template_name, {'form': form, })


class PostEditView(View):
    template_name = 'news/post_edit.html'
    form_class = PostForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={'post': Post.objects.get(pk=kwargs.get('pk')), })
        return render(request, self.template_name, {'form': form, })

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('posts:details', form.changed_data['pk'])
        return render(request, self.template_name, {'form': form, })
