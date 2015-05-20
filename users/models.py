from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    signature = models.CharField(max_length=255)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return unicode(self.username)
