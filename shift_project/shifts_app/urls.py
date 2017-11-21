from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^details/$', views.shift, name='shift'), #only an empty string will match
    url(r'^$', views.index, name='index'),
    url(r'^details/display$', views.display, name='shift'),
    url(r'^details/display/shift$', views.shifts_display, name='shift_display'),
    url(r'^details/group$', views.group, name='group'),
    url(r'^details/week$', views.week, name='group'),

]


