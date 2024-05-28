from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    # path('logout', auth_views.LogoutView.as_view(next_page='/login/', name='logout'),
]