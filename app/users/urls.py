from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from .views import signup_view, account_activation_sent_view, activate_account

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('account_activation_sent/', account_activation_sent_view, name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate_account, name='activate_account'),
]
