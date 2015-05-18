from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from hashids import Hashids


HASHER = Hashids(salt=settings.SECRET_KEY)


class Post(models.Model):
    message = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Foreign Keys
    thread = models.ForeignKey('threads.Thread')
    parent = models.OneToOneField('self', null=True, blank=True)

    def __str__(self):
        return self.slug

    def __unicode__(self):
        return u'%s' % self.slug


@receiver(post_save, sender=Post)
def generate_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = HASHER.encode(instance.pk)
        instance.save()
