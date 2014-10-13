# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('event_grouptalker', '0002_auto_20141013_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_pic',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ManyToManyField(related_name=b'events_user', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
