from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('recommendations/api/v1/', include('recommendations.urls')),
    path('admin/', admin.site.urls),
]
