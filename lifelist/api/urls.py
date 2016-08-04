from django.conf.urls import url
from api.views import *
from api import views

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^home', HomeView.as_view(), name='home'),
    url(r'^bucketlists/$', views.BucketlistList.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', views.BucketlistDetail.as_view()),
]
