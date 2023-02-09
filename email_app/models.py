# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AuthorSubscription(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, )
    subscribers = models.ManyToManyField(User, related_name='subscriptions', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SendedEmail(models.Model):
    subscription = models.ForeignKey(AuthorSubscription, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    opened = models.BooleanField(default=False)
