# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('event_grouptalker', '0003_auto_20141013_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='manager',
            field=models.ForeignKey(related_name=b'events_manager', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
