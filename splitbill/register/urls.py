from django.conf.urls import patterns, url

from register import views

urlpatterns = patterns('',
                       url(r'^', views.create, name='index'),
                       url(r'^create$', views.create, name='create'),
)