from django.urls import re_path
from tutorials import views

urlpatterns = [
    re_path(r'^api/tutorials$', views.tutorials_list),
    re_path('^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    re_path('^api/tutorials/published$', views.tutorial_list_published),
]
