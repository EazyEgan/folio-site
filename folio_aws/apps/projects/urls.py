
from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.IndexView.as_view(), name="project_index"),
    path('<int:pk>/', views.project_detail, name="project_detail"),

]
