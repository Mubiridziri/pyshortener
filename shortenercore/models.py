import datetime

from django.db import models
from django.utils import timezone


class Link(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('published date')
    original_link = models.CharField(max_length=500)

    def link_is_alive(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
