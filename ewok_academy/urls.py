"""
URL configuration for ewok_academy project.
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Built-in Django login / logout views
    path('login/', auth_views.LoginView.as_view(template_name='cafeteria/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Cafeteria app routes
    path('', include('cafeteria.urls')),
]
