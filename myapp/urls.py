from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
     path('hello/<int:id>', views.helo),
    path('projects/', views.get_projects, name='projects'),
     path('projects/<int:id>', views.get_project, name='project'),
     path('projects/create', views.create_project, name='create_project'),
     path('projects/<int:id>/update', views.update_project.as_view(), name='update_project'),
     path('projects/<int:id>/delete', views.delete_project, name='delete_project'),
    path('projects/<int:id>/tasks', views.get_project_tasks, name='project_tasks'),
     path('tasks/<int:id>', views.get_tasks, name='task'),
    path('tasks/', views.get_tasks, name='tasks'),
        path('tasks/create', views.create_task, name='create_task'),
        path('tasks/<int:id>/update', views.update_task.as_view(), name='update_task'),
    
]
