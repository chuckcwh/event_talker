# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_grouptalker', '0005_auto_20141013_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(null=True, upload_to=b'post_pics', blank=True),
        ),
    ]
