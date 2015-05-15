from django.db import models
from django.utils.text import slugify


class VisibleManager(models.Manager):
    def get_queryset(self):
        return super(VisibleManager, self).get_queryset().filter(active=True)


class Forum(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

    # Manager
    objects = models.Manager()
    visible = VisibleManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Forum, self).save(*args, **kwargs)
