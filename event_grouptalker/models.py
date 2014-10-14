from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Event(models.Model):
    SPORTS = "Sports"
    EDUCATION = "Education"
    TECHNOLOGY = "Technology"
    THREE_C = "3C"
    LIFE = "Life"
    OTHERS = "Others"
    CAT_FIELD = (
        (SPORTS, "Sports"),
        (EDUCATION, "Education"),
        (TECHNOLOGY, "Technology"),
        (THREE_C, "3C"),
        (LIFE, "Life"),
        (OTHERS, "Others"),
    )
    category = models.CharField(max_length=20,
                                choices=CAT_FIELD,
                                default=SPORTS)
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    event_pic = models.ImageField(upload_to="event_pics", null=True, blank=True)
    manager = models.ForeignKey(User, related_name='events_manager', null=True, blank=True)
    user =  models.ManyToManyField(User, related_name='events_user', null=True, blank=True)

    def __unicode__(self):
        return u"{}".format(self.title)

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    # post_pic = models.ImageField(upload_to="post_pics", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    
    # could just be "posts" for related name here
    event = models.ForeignKey(Event, related_name='posts_event')
    user = models.ForeignKey(User, related_name='posts_user')

    def __unicode__(self):
        return u"{}".format(self.title)

class Comment(models.Model):
    # could just be "comments" for related name here
    user = models.ForeignKey(User, related_name='comments_user')
    body = models.TextField()
    edit_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{}".format(self.body)
