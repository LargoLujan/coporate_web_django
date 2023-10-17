from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from .models import News, Event, Request, Profile
from .forms import NewsForm, RequestForm, ProfileUpdateForm, EventForm
from django.http import HttpResponseForbidden


def user_is_admin(user):
    return user.groups.filter(name='admin').exists()


def user_is_head(user):
    return user.groups.filter(name='head').exists()


def user_is_employees(user):
    return user.groups.filter(name='employees').exists()


def user_is_head_or_admin(user):
    return user_is_head(user) or user_is_admin(user)


def home(request):
    news = News.objects.all()
    return render(request, 'home.html', {'home': news})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    user_profile = request.user.profile
    user_is_admin = request.user.profile.position == 'admin'  # Cambia esto según cómo determinas que un usuario es admin en tu modelo
    return render(request, 'profile.html', {'profile': user_profile, 'user_is_admin': user_is_admin})


@login_required
def calendar(request, user_id=None):
    if user_id:
        events = Event.objects.filter(user_id=user_id)
    else:
        events = Event.objects.filter(user=request.user)
    return render(request, 'employees/calendar.html', {'events': events})


@login_required
@user_passes_test(user_is_head_or_admin)
def manage_requests(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_requests')
    else:
        form = RequestForm()
    return render(request, 'employees/manage_requests.html', {'form': form})


@login_required
@user_passes_test(user_is_head_or_admin)
def manage_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'employees/manage_news.html', {'form': form})


@login_required
def view_requests(request):
    requests = Request.objects.all()
    return render(request, 'employees/view_requests.html', {'requests': requests})


@login_required
@user_passes_test(user_is_head_or_admin)
def edit_profile(request, profile_id):
    # Verificar si el usuario es un administrador o líder
    if not user_is_head_or_admin(request.user):
        return HttpResponseForbidden()

    profile = get_object_or_404(Profile, id=profile_id)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
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

            # Asignar al grupo de trabajo (Position)
            user.groups.clear()
            user.groups.add(form.cleaned_data['position'])

            # Redireccionando a la vista de perfiles
            return redirect('manage_profiles')  # Redirigir a la lista de perfiles
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

    return render(request, 'edit_profile.html', {'form': form})




@login_required
@user_passes_test(user_is_head_or_admin)
def manage_profiles(request):
    users = User.objects.all()
    return render(request, 'edit_profile.html', {'users': users})
