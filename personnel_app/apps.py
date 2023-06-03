from django.apps import AppConfig


class PersonnelAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personnel_app'

    def ready(self) -> None:
        import personnel_app.signals
        return super().ready()