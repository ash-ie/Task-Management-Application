

from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from user_app.views import SigninAPIView, TaskListAPIView, TaskReportAPIView



urlpatterns = [
    path('refresh-token-access/', jwt_views.TokenRefreshView.as_view(), name='refresh-token-access'),
    path('user_signin/', SigninAPIView.as_view(), name='user_signin'),
    path('tasks/',TaskListAPIView.as_view(),name='tasks'),
    path('tasks/<int:pk>/',TaskListAPIView.as_view(),name='tasks'),
    path('tasks/<int:pk>/report/',TaskReportAPIView.as_view(),name='tasks'),
]