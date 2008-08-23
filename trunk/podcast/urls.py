from django.conf.urls.defaults import *

urlpatterns = patterns('podcast.views',
    # Show list of all shows
    (r'^$', 'show_list'),

    # Episode list of one show
    (r'^(?P<slug>[-\w]+)/$', 'episode_list'),

    # Episode detail of one show
    (r'^(?P<show_slug>[-\w]+)/(?P<episode_slug>[-\w]+)/$', 'episode_detail'),

    # Episode feed of one show
    (r'^(?P<slug>[-\w]+)/feed/$', 'episode_feed'),

    # Episode sitemap list of one show
    (r'^(?P<slug>[-\w]+)/sitemap.xml$', 'episode_sitemap'),
)