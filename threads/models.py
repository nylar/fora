from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from hashids import Hashids


HASHER = Hashids(salt=settings.SECRET_KEY)


class Thread(models.Model):
    subject = models.CharField(max_length=100)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    # Relations
    forum = models.ForeignKey('forums.Forum')

    # Managers
    objects = models.Manager()

    def __str__(self):
        return self.subject

    def __unicode__(self):
        return u'%s' % self.subject


@receiver(post_save, sender=Thread)
def generate_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = HASHER.encode(instance.pk)
        instance.save()
