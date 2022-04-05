from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage, name="home"),
    path('inbox/',views.inboxPage, name="inbox"),
    path('project/<str:pk>/',views.projectPage, name="project"),
]