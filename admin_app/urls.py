from django.urls import path

from admin_app import views

urlpatterns = [
    path('admin_home/',views.admin_index,name='admin_home'),
    path('add_task_admin/',views.add_task,name='add_task_admin'),
    path('view_task_admin/',views.view_task,name='view_task_admin'),
    path('edit_task_admin/<int:task_id>/',views.edit_task,name='edit_task_admin'),
    path('delete_task_admin/<int:task_id>/',views.delete_task,name='delete_task_admin'),
]