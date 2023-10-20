from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
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
    path('manage_news/', views.manage_news, name='manage_news'),
    path('add_news/', views.add_news, name='add_news'),
    path('edit_news/<int:news_id>/', views.edit_news, name='edit_news'),
    path('delete_news/<int:news_id>/', views.delete_news, name='delete_news'),
    path('delete_request/<int:request_id>/', views.delete_request, name='delete_request'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)