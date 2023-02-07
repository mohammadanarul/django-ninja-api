from django.contrib import admin
from django.urls import path, include
from blog.api.api import blogApi

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/blog/', blogApi.urls)
]
