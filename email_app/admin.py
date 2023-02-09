# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from email_app.models import *

# Register your models here.
admin.site.register(SendedEmail)
admin.site.register(AuthorSubscription)