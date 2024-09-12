from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("public/", include("public.urls")),
    path('api/', include("api.urls")),
    path("admin/", admin.site.urls),
]