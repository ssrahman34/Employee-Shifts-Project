from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^details/$', views.shift, name='shift'), #only an empty string will match
    url(r'^$', views.index, name='index'),
    url(r'^details/display$', views.display, name='shift'),
    url(r'^details/display/shift$', views.shifts_display, name='shift_display'),
    url(r'^details/group$', views.group, name='group'),
    url(r'^details/week$', views.week, name='group'),
    url(r'^index$',views.IndexView.as_view() ,name = 'index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name = 'detail'),
    #shift/shift/add/
    url(r'shift/add/$', views.ShiftCreate.as_view(), name = 'shift-add'),
    #shift/update/2
    url(r'shift/(?P<pk>[0-9]+)$', views.ShiftUpdate.as_view(), name = 'shift-update'),
    #shift/delete/2
    url(r'shift/(?P<pk>[0-9]+)/delete$',views.ShiftDelete.as_view(), name = 'shift-delete'),

]


