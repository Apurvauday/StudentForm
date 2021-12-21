from django.urls import path
from infoapp import views

urlpatterns = [
    path('student/', views.student_view),
]
