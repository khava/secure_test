from django.urls import path, include

from accounts import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('account/rest-auth/', include('rest_auth.urls')),
    path('account/register/', views.UserCreate.as_view()),
]