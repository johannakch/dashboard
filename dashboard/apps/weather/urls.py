from django.conf.urls import url
from apps.weather import views

urlpatterns = [
    url(r'^$', views.weather, name='weather')

]