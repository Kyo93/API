from django.urls import path
from profiles_user import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
