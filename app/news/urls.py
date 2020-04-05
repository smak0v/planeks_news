from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import PostsListView, PostCreateView, PostDetailView, PostEditView

urlpatterns = [
    path('', PostsListView.as_view(), name='main'),
    path('create/', login_required(PostCreateView.as_view()), name='create'),
    path('edit/<int:pk>/', login_required(PostEditView.as_view()), name='edit'),
    path('details/<int:pk>/', PostDetailView.as_view(), name='details'),
]

app_name = 'posts'
