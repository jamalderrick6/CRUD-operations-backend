from django.conf.urls import url 
from . import views 
 
urlpatterns = [ 
    url(r'^api/songs$', views.song_list),
    url(r'^api/songs/(?P<pk>[0-9]+)$', views.tutorial_detail),
]