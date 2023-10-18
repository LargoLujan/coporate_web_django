from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('manage_requests/', views.manage_requests, name='manage_requests'),
    path('manage_news/', views.manage_news, name='manage_news'),
    path('view_requests/', views.view_requests, name='view_requests'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('edit-profile/<int:profile_id>/', views.edit_profile, name='edit_profile'),
    path('manage-profiles/', views.manage_profiles, name='manage_profiles'),
    path('view_request/<int:request_id>/', views.view_single_request, name='view_single_request'),
    path('edit_request/<int:request_id>/', views.edit_request, name='edit_request'),

]

