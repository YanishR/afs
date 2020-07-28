from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
        path('profile/', views.ProfileView.as_view(), name='profile'),
        path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
        path('tasks/', views.TasksView.as_view(), name='tasks'),
        path('timesheet/', views.TimesheetView.as_view(), name='timesheet'),
        path('edit/', views.EditView.as_view(), name='edit'),
        path('test/', views.TestView.as_view(), name='test'),
        path('jobs/', views.JobsView.as_view(), name='jobs'),
        path('jobs/<int:pk>', views.JobView.as_view(), name='job')
        ]
        
