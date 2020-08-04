from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class AdminConfig(DjangoSuitConfig):
    layout = 'horizontal'

class MgbConfig(AppConfig):
    name = 'Mgb'

    def ready(self):
        import Mgb.signals
