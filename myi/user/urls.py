from django.urls import path

from .views import *
from .api_views import *

urlpatterns = [
   path("signup", UserCreateView.as_view()),
   path("login", UserLoginView.as_view()),
   path("alumni", AlumniCreateView.as_view()),
   path("alumni/detail/<int:pk>", AlumniDetailView.as_view()),
   path("alumni/update/<int:pk>", StudentUpdateView.as_view()),
   path("api/alumni", AlumniCreateApiView.as_view()),
   path("api/alumni/detail/<int:pk>", AlumniRetrieveApiView.as_view()),
   path("api/alumni/update/<int:pk>", AlumniUpdateApiView.as_view()),
   path("student", StudentCreateView.as_view()),
   path("student/update/<int:pk>", StudentUpdateView.as_view()),
   path("api/student", StudentCreateApiView.as_view()),
   path("student/detail/<int:pk>", StudentDetailView.as_view()),
   path("api/student/detail/<int:pk>", StudentRetrieveApiView.as_view()),
   path("api/student/update/<int:pk>", StudentUpdateApiView.as_view()),
]