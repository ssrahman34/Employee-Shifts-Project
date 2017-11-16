from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.shift, name='shift'), #only an empty string will match
     url(r'^$', views.index, name='index'),
]


