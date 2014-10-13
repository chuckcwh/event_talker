from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from event_grouptalker.models import Event, Post


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")

class EventForm(forms.ModelForm):
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
    category = forms.ChoiceField(choices=CAT_FIELD)

    title = forms.CharField(required=True)

    class Meta:
        model = Event
        fields = ("category", "title", "event_pic")

class PostForm(forms.ModelForm):
    title = forms.CharField(required=True)
    body = forms.CharField(required=True)

    class Meta:
        model = Post
        fields = ("title", "body")
