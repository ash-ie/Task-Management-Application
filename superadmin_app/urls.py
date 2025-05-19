from django.urls import path

from superadmin_app import views


urlpatterns = [
    path('',views.signin,name='signin'),
    path('superadmin_home',views.superadmin_index,name='superadmin_home'),
]