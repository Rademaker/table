from django.conf.urls import patterns, include, url
from roller.views import HomeView, TableView, TableListView, RollView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'table.views.home', name='home'),
    url(r'^home/?$', HomeView.as_view(), name='home'),
    url(r'^table_list/?$', TableListView.as_view(), name='table_list'),
    url(r'^table/(?P<pk>\d+)/?$', TableView.as_view(), name='table'),
    url(r'^roll/?$', RollView.as_view(), name='table'),
)

