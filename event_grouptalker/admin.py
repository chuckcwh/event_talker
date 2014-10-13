from django.contrib import admin

# Register your models here.
from event_grouptalker.models import Comment, Post, Event

admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Comment)