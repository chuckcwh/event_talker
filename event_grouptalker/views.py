import json
from operator import itemgetter
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
import facebook

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import time
from event_grouptalker.forms import EmailUserCreationForm, EventForm, PostForm
from event_grouptalker.models import Event, Post
from event_talker import settings

def home(request):
    return render(request, 'home.html')

def event_list(request):
    events = Event.objects.all()
    data = {'events': events}
    return render(request, 'event_list.html', data)

def view_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # the PostForm's save() method should be able to handle creating this
            Post.objects.create(title=form.cleaned_data['title'],
                                body=form.cleaned_data['body'],
                                # post_pic=form.cleaned_data['post_pic'],
                                event=event,
                                user=request.user)
            event_page = "/event/" + str(event.id)
            return redirect(event_page)
    else:
        form = PostForm()
    data = {'form': form, "event": event}
    return render(request, 'view_event.html', data)

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            # the EventForm's save() method should be able to handle creating this
            Event.objects.create(category=form.cleaned_data['category'],
                                 title=form.cleaned_data['title'],
                                 event_pic=form.cleaned_data['event_pic'])
            return redirect("event_list")
    else:
        form = EventForm()
    data = {'form': form}
    return render(request, 'add_event.html', data)

def post_of_day(request):
    collection = []
    posts = Post.objects.all()
    for post in posts:
        collection.append({
            'title': post.title,
            'body': post.body,
            'edit_time': post.edit_time.isoformat(),
            'event': post.event,
            'user': post.user
        })

    return HttpResponse(json.dumps(collection),
                        content_type='application/json')


def faq(request):
    return render(request, 'faq.html')

@login_required
def profile(request):
    user_social_auth = request.user.social_auth.filter(provider='facebook').first()
    if user_social_auth:
        graph = facebook.GraphAPI(user_social_auth.extra_data['access_token'])
        profile_data = graph.get_object("me")
        return render(request, 'profile.html', profile_data)
    else:
        return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            text_content = 'Thank you for signing up for our website at {}, {} {}'.format(user.date_joined, user.first_name, user.last_name)
            html_content = '<h2>Thanks {} {} for signing up at {}!</h2> <div>I hope you enjoy using our site</div>'.format(user.first_name, user.last_name, user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
      })
