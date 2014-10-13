# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_grouptalker', '0004_auto_20141013_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_pic',
            field=models.ImageField(null=True, upload_to=b'event_pics', blank=True),
        ),
    ]
