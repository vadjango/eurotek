from django.apps import AppConfig


class CodesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'report.auth.codes'
    label = 'report_auth_codes'

    def ready(self):
        import report.auth.codes.signals
