from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('app.tasks.urls')),
    path('users/', include('app.users.urls')),
    path('subjects/', include('app.subjects.urls')),
    path('api-token-auth/', views.obtain_auth_token),
]
