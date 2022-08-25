from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('user/', include('users.urls')),
    path('', include('tasks.urls')),
    path('admin/', admin.site.urls),
]
