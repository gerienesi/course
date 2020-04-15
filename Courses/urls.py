from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/course/', include('courseApp.api.urls')),  # courses endpoint
    path(r'api/student/', include('studentApp.api.urls')),  # students endpoint
]
