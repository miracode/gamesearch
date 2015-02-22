from django.conf.urls import patterns, include, url
from django.contrib import admin

from search import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gamesdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'search.views.index', name='home'),
    url(r'^results/', 'search.views.results', name='results'),
    # url(r'^games/$', views.GameView.as_view(), name='game-list')
    url(r'^api/(?P<name>\w+)$',
        views.GameView.as_view()),
    url(r'^api/$', 'search.views.api', name='api'),
)
