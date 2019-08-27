from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CRMConfig(AppConfig):
    name = "worktest.crm"
    verbose_name = _("CRM")

    def ready(self):
        try:
            import worktest.users.signals  # noqa F401
        except ImportError:
            pass
