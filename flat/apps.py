# -*- coding: utf-8 -*-

from django.apps import AppConfig


class FlatConfig(AppConfig):
    name = 'flat'
    verbose_name = 'Django flat theme'

    def ready(self):
        from flat import settings

        settings.check_installed_apps()
