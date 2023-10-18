# Proyecto Web Corporativo

Este proyecto web corporativo es una plataforma diseñada para una empresa con tres grupos de trabajo: administradores (admin), jefes de equipo (head) y empleados (employees). Permite a los usuarios realizar solicitudes, ver su perfil y acceder a noticias de la empresa. Además, ofrece funciones adicionales para los grupos de administradores y jefes de equipo, como la gestión de solicitudes, perfiles y noticias.

## Características Principales

- **Autenticación de Usuarios**: Los usuarios deben iniciar sesión para acceder a las funciones de la plataforma. La autenticación se gestiona mediante un sistema de inicio de sesión y cierre de sesión.

- **Grupos de Trabajo**: Los usuarios se dividen en tres grupos: administradores, jefes de equipo y empleados. Cada grupo tiene diferentes niveles de acceso y permisos en la plataforma.

- **Solicitudes**: Los usuarios pueden enviar solicitudes a través de la plataforma. Los jefes de equipo y administradores pueden gestionar estas solicitudes, aprobarlas o rechazarlas.

- **Perfiles de Usuario**: Los usuarios pueden ver sus perfiles personales. Los administradores tienen acceso a la gestión de perfiles de todos los usuarios.

- **Noticias de la Empresa**: Los usuarios pueden acceder a noticias relacionadas con la empresa y mantenerse actualizados sobre eventos y anuncios importantes.

## Uso de la Aplicación

1. **Inicio de Sesión**:
   - Abre la aplicación en tu navegador web.
   - Inicia sesión con tu nombre de usuario y contraseña.

2. **Página Principal**:
   - Después de iniciar sesión, serás dirigido a la página principal.
   - Aquí podrás ver noticias de la empresa y las solicitudes pendientes (si eres jefe de equipo o administrador).

3. **Solicitudes**:
   - Desde la página principal, los jefes de equipo y administradores pueden acceder a la sección de solicitudes para gestionarlas.

4. **Perfil**:
   - En la página de perfil, puedes ver y editar tu información personal.
   - Los administradores pueden acceder a la gestión de perfiles de usuario desde esta página.

5. **Noticias**:
   - La sección de noticias te permite acceder a las noticias de la empresa para mantenerte informado.

6. **Cerrar Sesión**:
   - En cualquier momento, puedes cerrar sesión haciendo clic en "Cerrar Sesión" en la parte superior de la página.

## Roles de Usuario

- **Administradores (admin)**:
   - Acceso completo a todas las funciones.
   - Gestión de solicitudes, perfiles y noticias.
   
- **Jefes de Equipo (head)**:
   - Acceso a solicitudes y perfiles.
   - Pueden gestionar solicitudes de su equipo.

- **Empleados (employees)**:
   - Acceso limitado a ver su perfil y noticias.
   - Pueden enviar solicitudes.

## Requisitos del Sistema

- Python 3.x
- Django Framework
- Base de datos (por ejemplo, SQLite)

## Instalación y Configuración

1. Clona este repositorio a tu máquina local.
2. Crea un entorno virtual y actívalo.
3. Instala las dependencias del proyecto utilizando `pip install -r requirements.txt`.
4. Configura la base de datos en el archivo `settings.py` según tu preferencia (por defecto, se utiliza SQLite).
5. Realiza las migraciones de la base de datos con `python manage.py migrate`.
6. Crea un superusuario con `python manage.py createsuperuser` para acceder al panel de administración.
7. Inicia el servidor de desarrollo con `python manage.py runserver`.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar o expandir este proyecto, siéntete libre de hacer un fork y enviar pull requests.

## Créditos

Este proyecto fue desarrollado por Manuel Lujan vilchez.

