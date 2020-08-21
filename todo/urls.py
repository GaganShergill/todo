from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='taskList'),
    path('add/', views.TaskCreateView.as_view(), name='taskAdd'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='taskUpdate'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='taskDelete'),
    path('<int:pk>/Complete/', views.TaskCompleteView, name='taskComplete'),
    path('<int:pk>/NotComplete/', views.TaskNotCompleteView, name='taskNotComplete'),
]
