import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Link(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    original_link = models.CharField(max_length=500)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def is_alive(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
