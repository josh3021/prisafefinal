from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from primus import views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^service/$', views.service, name='service'),
    url(r'^signup/$', views.signup, name='signup'),
]
