from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path("whiteboard/", include("chat.urls")),  # Includes chat app URLs under /whiteboard/
    path("admin/", admin.site.urls),  # Admin interface URL
    path("", include("home.urls")),
]
