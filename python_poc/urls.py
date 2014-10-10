from django.conf.urls import patterns, url

from pythonweb.controllers.usercontroller import UserController


urlpatterns = patterns('',
    url(r'^users/(?P<userid>[0-9]+)/$', UserController.as_view()),
)
