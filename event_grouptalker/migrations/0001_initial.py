# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(related_name=b'comments_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'Sports', max_length=20, choices=[(b'Sports', b'Sports'), (b'Education', b'Education'), (b'Technology', b'Technology'), (b'3C', b'3C'), (b'Life', b'Life'), (b'Others', b'Others')])),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('event_pic', models.ImageField(upload_to=b'')),
                ('manager', models.ForeignKey(related_name=b'events_manager', to=settings.AUTH_USER_MODEL)),
                ('user', models.ManyToManyField(related_name=b'events_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('post_pic', models.ImageField(upload_to=b'')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(related_name=b'posts_event', to='event_grouptalker.Event')),
                ('user', models.ForeignKey(related_name=b'posts_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
