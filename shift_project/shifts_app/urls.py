from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main/$', views.shift, name='shift'), #only an empty string will match
    url(r'^$', views.index, name='index'),
    url(r'^details/display$', views.display, name='shift'),
    url(r'^details/display/shift$', views.shifts_display, name='shift_display'),
    url(r'^details/group$', views.group, name='group'),
    url(r'^details/week$', views.week, name='group'),
    url(r'^index$',views.IndexView.as_view() ,name = 'index'),
    url(r'^users/$', views.user, name='users'),
    url(r'^users/details/(?P<usr_id>[0-9]+)$', views.Userview, name='userview'),
    url(r'^covered/(?P<shift_id>[0-9]+)/$',views.covered, name = 'covered'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name = 'detail'),
    #shift/shift/add/
    url(r'shift/add/$', views.ShiftCreate.as_view(), name = 'shift-add'),
    #url(r'run/add/(?P<pk>[0-9]+)$', views.RunCreate.as_view(), name = 'run-add'),
    url(r'^(?P<shift_id>[0-9]+)/create_run/$', views.create_run, name='create_run'),
    #shift/update/2
    url(r'shift/(?P<pk>[0-9]+)$', views.ShiftUpdate.as_view(), name = 'shift-update'),
    #shift/delete/2
    url(r'shift/(?P<pk>[0-9]+)/delete$',views.ShiftDelete.as_view(), name = 'shift-delete'),
    #run/shift_id/user_id
    url(r'^(?P<shift_id>\d+)/edit/(?P<run_id>[0-9]+)$', views.edit_run, name='edit_run'),
    url(r'run/(?P<shift_id>[0-9]+)/(?P<usr_id>[0-9]+)$',views.run_update, name = 'run-update'),

]


