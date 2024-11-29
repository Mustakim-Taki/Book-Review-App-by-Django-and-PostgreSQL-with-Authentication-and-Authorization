from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from reviews import views  # Import your app's views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
]
