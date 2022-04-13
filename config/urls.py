from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tick_tick_school.tasks.urls'), name="tasks"),
    path('users/', include('tick_tick_school.users.urls'), name="users"),
    path('subjects/', include('tick_tick_school.subjects.urls'), name="subjects"),
    path('api-token-auth/', views.obtain_auth_token)
]
