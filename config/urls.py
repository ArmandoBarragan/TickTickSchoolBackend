from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('tasks/', include('tick_tick_school.tasks.urls')),
    # path('users/', include('tick_tick_school.users.urls')),
    # path('subjects/', include('tick_tick_school.subjects.urls'))
]
