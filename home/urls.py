from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    # Outras URLs
]
