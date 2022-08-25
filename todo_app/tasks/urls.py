from django.urls import path

from .views import CreateTask, DeleteTask, FilterGet, GetAllTasks, UpdateTask

urlpatterns = [
    path('create_task/', CreateTask, name='create_task'),
    path('delete_task/<str:pk>/', DeleteTask, name='delete_task'),
    path('get_all_tasks/', GetAllTasks, name='get_all_tasks'),
    path('update_task/<str:pk>/', UpdateTask, name='update_task'),
    path('get_task/', FilterGet.as_view(), name='update_task'),
]
