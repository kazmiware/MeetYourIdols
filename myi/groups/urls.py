from django.urls import path

from .views import *
from .api_views import *


urlpatterns = [
   path('post/add/<int:pk>', AddPostView.as_view(), name="add_post"),
   path('api/group', GroupCreateApiView.as_view()),
   path('group', GroupCreateView.as_view()),
   path('group/detail/<int:pk>', GroupDetailView.as_view(), name="group_detail"),
   path('api/group/detail/<int:pk>', GroupDetailApiView.as_view())
]