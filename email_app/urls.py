from django.conf.urls import url

from email_app import views

urlpatterns = [
    url(r"open-tracking/(?P<email_id>\d+)/$", views.PixelView.as_view(), name="pixel_view"),
    url(r"send/", views.send_subscribers, name="sendmail"),
]