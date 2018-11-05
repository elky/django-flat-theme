# -*- coding: utf-8 -*-

import django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def check_installed_apps():
    dj_version = django.VERSION
    installed_apps = settings.INSTALLED_APPS

    if dj_version < (1, 9):
        if 'flat' not in installed_apps:
            raise ImproperlyConfigured(
                '\'flat\' needed before django 1.9, '
                'add it to settings.INSTALLED_APPS.')
    else:
        if 'flat' in installed_apps:
            raise ImproperlyConfigured(
                '\'flat\' not needed since django 1.9, '
                'remove it from settings.INSTALLED_APPS.')
