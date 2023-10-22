from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from .models import News, Event, Request, Profile
from .forms import NewsForm, RequestForm, ProfileUpdateForm, EditRequestForm
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib import messages


# Función para verificar si el usuario es miembro del grupo 'admin'
def user_is_admin(user):
    return user.groups.filter(name='admin').exists()


# Función para verificar si el usuario es miembro del grupo 'head'
def user_is_head(user):
    return user.groups.filter(name='head').exists()


# Función para verificar si el usuario es miembro del grupo 'employees'
def user_is_employees(user):
    return user.groups.filter(name='employees').exists()


# Función para verificar si el usuario es miembro de los grupos 'admin' o 'head'
def user_is_head_or_admin(user):
    return user_is_head(user) or user_is_admin(user)


# Vista para la página de inicio
def home(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'news': news})


# Función para verificar si el usuario tiene permisos adecuados
def user_has_permission(user):
    # Comprobar si el usuario pertenece a los grupos 'admin' o 'head'.
    return user.groups.filter(name__in=['admin', 'head']).exists()


# Vista para cerrar sesión
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# Vista para el perfil de usuario
@login_required
def profile(request):
    user_profile = request.user.profile
    user_is_admin = request.user.profile.position == 'admin'  # Cambia esto según cómo determinas que un usuario es admin en tu modelo
    return render(request, 'profile.html', {'profile': user_profile, 'user_is_admin': user_is_admin})


# Vista para las solicitudes de usuario
@login_required
def manage_requests(request):
    if request.method == "POST":
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_model = form.save(commit=False)
            request_model.user = request.user
            request_model.save()
            return redirect('manage_requests')
    else:
        form = RequestForm()

    # Aquí recuperamos todas las solicitudes
    requests = Request.objects.filter(user=request.user)
    return render(request, 'manage_requests.html', {'form': form, 'requests': requests})


# Vista para gestionar noticias
@login_required
@user_passes_test(user_has_permission, login_url='/without_permission/')
def manage_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    # Redireccionando a la gestion de noticias
    return render(request, 'manage_news.html', {'form': form})


# Vista para ver todas las solicitudes
@login_required
def view_requests(request):
    all_requests = Request.objects.all().order_by('-created_at')
    # Redireccionando a la vista de para ver las solicitudes
    return render(request, 'view_requests.html', {'requests': all_requests})


# Vista para editar el perfil de usuario
@login_required
@user_passes_test(user_has_permission, login_url='/without_permission/')
def edit_profile(request, profile_id):
    # Verificar si el usuario es un admin o head
    if not user_is_head_or_admin(request.user):
        return HttpResponseForbidden()

    profile = get_object_or_404(Profile, id=profile_id)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Aquí se actualiza los datos del usuario
            user = profile.user
            user.username = form.cleaned_data['user_username']
            user.email = form.cleaned_data['user_email']
            user.first_name = form.cleaned_data['user_first_name']
            user.last_name = form.cleaned_data['user_last_name']
            # Solo cambia la contraseña si se ingresó una nueva
            new_password = form.cleaned_data['user_password']
            if new_password:
                user.set_password(new_password)
            user.save()

            # Guardando datos del Profile
            form.save()

            # Asignar al grupo de trabajo
            user.groups.clear()
            user.groups.add(form.cleaned_data['position'])

            # Redireccionando a la vista de perfiles
            return redirect('manage_profiles')
        else:
            # Imprimir errores del formulario si no es válido
            print(form.errors)
    else:
        form = ProfileUpdateForm(instance=profile, initial={
            'user_username': profile.user.username,
            'user_email': profile.user.email,
            'user_first_name': profile.user.first_name,
            'user_last_name': profile.user.last_name
        })

    return render(request, 'edit_profile.html', {'form': form, 'editing': True})


# Vista para gestionar perfiles
@login_required
@user_passes_test(user_has_permission, login_url='/without_permission/')
def manage_profiles(request):
    users = User.objects.all()
    return render(request, 'edit_profile.html', {'users': users, 'editing': False})


# Vista para ver una solicitud individual
@login_required
def view_single_request(request, request_id):
    single_request = get_object_or_404(Request, id=request_id)
    if single_request.user != request.user:
        return HttpResponseForbidden("No tienes permiso para ver esta solicitud.")
    context = {'single_request': single_request}
    return render(request, 'single_request.html', context)


# Vista para editar una solicitud
@login_required
@user_passes_test(user_has_permission, login_url='/without_permission/')
def edit_request(request, request_id):
    request_instance = get_object_or_404(Request, id=request_id)

    if request.method == 'POST':
        form = EditRequestForm(request.POST, instance=request_instance)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditRequestForm(instance=request_instance)

    context = {
        'form': form,
    }
    return render(request, 'edit_request.html', {'form': form})


# Vista para gestionar noticias
@login_required
@user_passes_test(user_has_permission, login_url='/without_permission/')
def manage_news(request):
    news = News.objects.all()
    return render(request, 'manage_news.html', {'news': news})


# Vista para agregar una noticia
@login_required
@user_passes_test(user_has_permission, login_url='/without_permission/')
def add_news(request):
    if request.method == "POST":
        news_form = NewsForm(request.POST, request.FILES)
        if news_form.is_valid():
            # Procesar y guardar el formulario si es válido
            news_form.save()
            return redirect('manage_news')
    else:
        news_form = NewsForm()

    return render(request, 'add_news.html', {'news_form': news_form})


# Vista para editar una noticia
@login_required
@user_passes_test(user_has_permission, login_url='/without_permission/')
def edit_news(request, news_id):
    news = News.objects.get(pk=news_id)

    if request.method == "POST":
        news_form = NewsForm(request.POST, request.FILES, instance=news)
        if news_form.is_valid():
            news_form.save()
            return redirect('manage_news')
    else:
        news_form = NewsForm(instance=news)

    return render(request, 'edit_news.html', {'news_form': news_form, 'news': news})


# Vista para eliminar una noticia
@login_required
@user_passes_test(user_has_permission, login_url='/without_permission/')
def delete_news(request, news_id):
    news = News.objects.get(pk=news_id)

    if request.method == "POST":
        news.delete()
        return redirect('manage_news')

    return render(request, 'confirm_delete_news.html', {'news': news})


# Vista para eliminar una solicitud
@login_required
@user_passes_test(user_has_permission, login_url='/without_permission/')
def delete_request(request, request_id):
    request_to_delete = get_object_or_404(Request, id=request_id)

    # Verifica si el usuario es el creador de la solicitud o es un administrador
    if request.user == request_to_delete.user or request.user.is_superuser:
        if request.method == 'POST':
            request_to_delete.delete()
            messages.success(request, "La solicitud ha sido eliminada exitosamente.")
            return redirect('view_requests')
        else:
            return render(request, 'confirm_delete_request.html', {'request_to_delete': request_to_delete})
    else:
        messages.error(request, "No tienes permiso para eliminar esta solicitud.")
        return redirect('view_requests')


# Vista para usuarios sin permisos
def without_permission(request):
    return render(request, 'without_permission.html')
