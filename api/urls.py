from django.urls import path 
from . import views

urlpatterns = [
    path('getFeedbackData',views.getData),
    path('addFeedbackData',views.addFeedback),
]