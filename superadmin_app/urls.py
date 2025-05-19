from django.urls import path

from superadmin_app import views


urlpatterns = [
    path('',views.signin,name='signin'),
    path('superadmin_home/',views.superadmin_index,name='superadmin_home'),
    path('add_users/',views.add_users,name='add_users'),
    path('view_users/',views.view_users,name='view_users'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
]