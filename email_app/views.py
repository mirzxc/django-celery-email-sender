# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import HttpResponse
from django.views import View

from tasks import *


def send_subscribers(request):
    # send_letter.delay(request.user.id)
    send_letter.apply_async((request.user.id, ), countdown=10)
    return HttpResponse("Check your mail please")


class PixelView(View):

    def get(self, request, *args, **kwargs):
        PIXEL_GIF_DATA = """
        R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7
        """.strip().decode('base64')
        email_id = kwargs.get('email_id')
        email = SendedEmail.objects.filter(id=email_id).first()
        email.opened = True
        email.save()
        return HttpResponse(PIXEL_GIF_DATA, content_type='image/gif')
