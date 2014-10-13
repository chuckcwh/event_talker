# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_grouptalker', '0006_auto_20141013_0645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_pic',
        ),
    ]
