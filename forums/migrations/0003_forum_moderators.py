# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forums', '0002_forum_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='moderators',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
