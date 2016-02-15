from django.conf.urls import patterns, include, url

from servers import views

urlpatterns = patterns('',
  url(r'^$', views.servers_list, name='servers_list'),
  url(r'^new$', views.server_create, name='new_server'),
  url(r'^edit/(?P<pk>\d+)$', views.server_update, name='server_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.server_delete, name='server_delete'),
)
