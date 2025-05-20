from django.urls import path

from superadmin_app import views


urlpatterns = [
    path('',views.signin,name='signin'),
    path('superadmin_home/',views.superadmin_index,name='superadmin_home'),
    path('add_users/',views.add_users,name='add_users'),
    path('view_users/',views.view_users,name='view_users'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('add_tasks/',views.add_task,name='add_tasks'),
    path('view_tasks/',views.view_task,name='view_tasks'),
    path('edit_task/<int:task_id>/',views.edit_task,name='edit_task'),
    path('delete_task/<int:task_id>/',views.delete_task,name='delete_task'),
    path('signout/',views.signout,name='signout')
]