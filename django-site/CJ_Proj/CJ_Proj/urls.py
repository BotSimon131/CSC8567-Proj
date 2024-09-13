from django.contrib import admin
from django.urls import include, path
from settings.py import LOCAL_APPS

urlpatterns = [
    path("admin/", admin.site.urls),
]

if "api" in LOCAL_APPS:
    urlpatterns += [
        path('api/', include("api.urls")),
    ]
if "public" in LOCAL_APPS:
    urlpatterns += [
        path("public/", include("public.urls")),
    ]