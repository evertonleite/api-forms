from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('apiForm/v1/', include('apiForm.urls', namespace='apiForm')),
    path('apiForm-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
