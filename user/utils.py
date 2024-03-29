from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.core.mail import EmailMessage
from .models import CustomUser


def send_email_verification(request, user):
    try:
        current_site = get_current_site(request)
        context = {
            'domain': current_site.domain,
            'user': user,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': token_generator.make_token(user)
        }
        message = render_to_string('verify_email.html', context=context)
        
        user.verification_token = context['token']
        user.save()
        
        email = EmailMessage('Verify email', message, to=[user.email])
        email.send()
    except Exception as e:
        print(f"Error sending email: {e}")


def send_email_reset_password(request, user):
    try:
        current_site = get_current_site(request)
        context = {
            'domain': current_site.domain,
            'user': user,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': token_generator.make_token(user)
        }
        message = render_to_string('verify_email_reset_password.html', context=context)
        
        user.verification_token = context['token']
        user.save()
        
        email = EmailMessage('Verify email', message, to=[user.email])
        email.send()
    except Exception as e:
        print(f"Error sending email: {e}")


