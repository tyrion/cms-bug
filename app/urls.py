from django.conf.urls import include, patterns, url

urlpatterns = patterns('app.views',
    url(r'^$', 'index'),
    url(r'^bug/$', 'bug'),
)
