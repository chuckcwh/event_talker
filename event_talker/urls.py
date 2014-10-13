from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'event_talker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # personal basic
    url('', include('social.apps.django_app.urls', namespace='social')),


    # main
    url(r'^$', 'event_grouptalker.views.home', name='home'),
    url(r'^profile/$', 'event_grouptalker.views.profile', name='profile'),
    url(r'^faq/$', 'event_grouptalker.views.faq', name='faq'),
    url(r'^event_list/$', 'event_grouptalker.views.event_list', name='event_list'),
    url(r'^event/new/$', 'event_grouptalker.views.add_event', name='add_event'),
    # url(r'^event/$', 'event_grouptalker.views.event', name='event'),
    url(r'^event/(?P<event_id>\w+)/$', 'event_grouptalker.views.view_event', name='view_event'),


    # ajax
    url(r'^post_of_day/$', 'event_grouptalker.views.post_of_day', name='post_of_day'),


    # systematic
    url(r'^register/$', 'event_grouptalker.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
