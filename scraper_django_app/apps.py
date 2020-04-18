from django.apps import AppConfig


class ScraperDjangoAppConfig(AppConfig):
    name = 'scraper_django_app'
    def ready(self):
        from updater import updater
        updater.start()
