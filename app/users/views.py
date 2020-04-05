from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode

from .forms import UserCreationForm
from .models import User
from .tokens import account_activation_token


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            html_message = render_to_string('email/account_activation.html', {
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user('Activate your PLANEKS News Account', strip_tags(html_message), html_message=html_message)
            return redirect('users:account_activation_sent')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, })


def account_activation_sent_view(request):
    return render(request, 'registration/account_activation_sent.html', {})


def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.is_confirmed_email = True
        user.save()
        login(request, user)
        return render(request, 'registration/account_activation_success.html', {})
    else:
        return render(request, 'registration/account_activation_invalid.html', {})
