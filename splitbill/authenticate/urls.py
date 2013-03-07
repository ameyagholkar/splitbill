from django.conf.urls import patterns, url

from authenticate import views

urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^authenticate', views.auth, name='auth'),
                url(r'^dashboard', views.load_dashboard, name='load_dashboard'),
                url(r'^logout', views.log_out, name='logout'),
                url(r'^testpage', views.testcontent, name='testcontent')
             )