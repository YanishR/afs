from django.urls import path, include

from . import views

app_name = 'emp'

urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
        path('', include('django.contrib.auth.urls')),
        path('test', views.TestView.as_view(), name='test'),
]
