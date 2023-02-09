from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from email_app.models import AuthorSubscription, SendedEmail


@shared_task
def send_letter(user_id):
    user_model = get_user_model()
    to_user = user_model.objects.get(id=user_id)
    author = AuthorSubscription.objects.get(author=to_user)

    mail = SendedEmail.objects.create(subscription=author)

    merge_data = {
        'user': to_user,
        'subscribers': author.subscribers.all(),
        'mail': mail,

    }
    html_body = render_to_string("custom_email.html", merge_data)

    message = EmailMultiAlternatives(
        subject='Subscribers',
        body="Your subscribers:",
        from_email=settings.EMAIL_HOST_USER,
        to=[to_user.email]
    )
    message.attach_alternative(html_body, "text/html")
    message.send(fail_silently=False)