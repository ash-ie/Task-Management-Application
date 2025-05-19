

from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from user_app import views


urlpatterns = [
    path('',views.index,name='index'),
    path('refresh-token-access/', jwt_views.TokenRefreshView.as_view(), name='refresh-token-access'),
]