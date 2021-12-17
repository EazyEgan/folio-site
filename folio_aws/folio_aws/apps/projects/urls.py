"""from django.urls import path

from . import views

#To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns to views.
app_name = 'projects'

urlpatterns = [
    # ex: /projects/
    path('', views.index, name='index'),
    # ex: /projects/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /projects/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /projects/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]"""

from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.IndexView.as_view(), name="project_index"),
    path('<int:pk>/', views.project_detail, name="project_detail"),

]
#path('<string:lang>', views.IndexView.as_view(), name="project_index"),
