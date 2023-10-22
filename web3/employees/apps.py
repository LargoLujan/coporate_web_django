from django.apps import AppConfig


# Esta clase define la configuración de la aplicación "employees".
class EmployeesConfig(AppConfig):
    # Especifica el tipo de campo que se utilizará por defecto para las IDs automáticas
    # en los modelos de esta aplicación cuando no se especifique un tipo de campo primario.
    default_auto_field = 'django.db.models.BigAutoField'

    # El nombre de la aplicación, que es 'employees' en este caso.
    name = 'employees'

    # La función ready se llama cuando Django está iniciando y ha cargado completamente esta aplicación.
    def ready(self):
        # Importamos los "signals" de la aplicación employees.
        # Los "signals" en Django son una forma de permitir que diferentes componentes
        # reaccionen a ciertos eventos. Por ejemplo, se puede usar un signal para
        # hacer algo cada vez que se guarda un modelo en la base de datos.
        import employees.signals

