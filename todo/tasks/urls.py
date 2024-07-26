from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name="index"),

    path('create-task/', views.create_task, name="create-task"),

    path('delete-task/<int:pk>/<task_type>/', views.delete_task, name='delete-task'),

    path('update-task/<int:pk>/<str:task_type>', views.update_task, name='update-task'),
    
    path('search-task/', views.search_task, name='search-task'),

]