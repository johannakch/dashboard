
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^complete/(?P<id>[0-9]+)/$', views.completeTodo, name='complete'),
    url(r'^deletecomplete/$', views.deleteCompleted, name='deletecomplete')
]