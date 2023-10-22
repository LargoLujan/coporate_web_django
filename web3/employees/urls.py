from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Definición de las rutas URL para esta aplicación.
urlpatterns = [
    # Ruta principal que muestra la página de inicio.
    path('', views.home, name='home'),

    # Ruta para la página de inicio de sesión con una plantilla personalizada.
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Ruta para cerrar sesión y redirigir al usuario a la página de inicio de sesión.
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Ruta para ver el perfil del usuario.
    path('profile/', views.profile, name='profile'),

    # Ruta para gestionar las solicitudes.
    path('manage_requests/', views.manage_requests, name='manage_requests'),

    # Ruta para gestionar las noticias.
    path('manage_news/', views.manage_news, name='manage_news'),

    # Ruta para ver todas las solicitudes.
    path('view_requests/', views.view_requests, name='view_requests'),

    # Ruta para editar el perfil con un ID específico.
    path('edit-profile/<int:profile_id>/', views.edit_profile, name='edit_profile'),

    # Ruta para gestionar los perfiles.
    path('manage_profiles/', views.manage_profiles, name='manage_profiles'),

    # Ruta para ver una solicitud específica según su ID.
    path('view_request/<int:request_id>/', views.view_single_request, name='view_single_request'),

    # Ruta para editar una solicitud específica según su ID.
    path('edit_request/<int:request_id>/', views.edit_request, name='edit_request'),

    # Ruta duplicada para gestionar las noticias, se debe considerar eliminar una de ellas.
    path('manage_news/', views.manage_news, name='manage_news'),

    # Ruta para añadir una noticia.
    path('add_news/', views.add_news, name='add_news'),

    # Ruta para editar una noticia específica según su ID.
    path('edit_news/<int:news_id>/', views.edit_news, name='edit_news'),

    # Ruta para eliminar una noticia específica según su ID.
    path('delete_news/<int:news_id>/', views.delete_news, name='delete_news'),

    # Ruta para eliminar una solicitud específica según su ID.
    path('delete_request/<int:request_id>/', views.delete_request, name='delete_request'),

    # Ruta para mostrar una página cuando el usuario no tiene permiso.
    path('without_permission/', views.without_permission, name='without_permission'),
]

# Si el proyecto está en modo DEBUG, añade las rutas para servir archivos multimedia.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
