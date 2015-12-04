Django Flat Theme
=================

**django-flat-theme** is included as `part <https://github.com/django/django/commit/35901e64b043733acd1687734274553cf994511b>`_ of Django from `version 1.9 <https://docs.djangoproject.com/en/1.9/releases/1.9/#new-styling-for-contrib-admin>`_! :tada:

Please use this app if your project is powered by an older Django version.

Description
-----------

**django-flat-theme** brings fresh air to the default Django Admin
interface which hasn't changed in 10 years, since the very first version of
Django framework. This theme makes the UI modern and clean.

This app overrides the default admin's CSS. All the changes only involve CSS:
colors, margins, sizes and icons; nothing major is changed.

Installation
------------

Install via pip:
``pip install django-flat-theme``

1. Put ``flat`` app in your *INSTALLED\_APPS* **before**
   ``django.contrib.admin``:

   ::

       INSTALLED_APPS = (
           ...
           'flat',
           'django.contrib.admin',
           ...
       )

2. Enjoy!

Compatibility
~~~~~~~~~~~~~

Works properly in Django 1.5+.

Font
~~~~

This theme uses the `Roboto font <http://www.google.com/fonts/specimen/Roboto>`__
which is under Apache 2.0 licence.

Testing
~~~~~~~

Tested in:

- Internet Explorer 7+ (IE8 and less doesn't support SVG so icons are not displayed)
- Firefox 30+ (Windows, Ubuntu, OS X)
- Chrome 35+ (Windows, Ubuntu, OS X)
- Safari 8 (OS X)

Screenshot Examples
~~~~~~~~~~~~~~~~~~~

**Login page**

|1|

------------

**Dashboard**

|2|

------------

**List of objects**

|3|

------------

**New object**

|4|

.. |1| image:: https://cloud.githubusercontent.com/assets/209663/9546175/f4c24520-4da9-11e5-9182-b5d791d4115f.png
.. |2| image:: https://cloud.githubusercontent.com/assets/209663/9546174/f4c1ddba-4da9-11e5-8781-c629a52cae0f.png
.. |3| image:: https://cloud.githubusercontent.com/assets/209663/9546176/f4fd6a24-4da9-11e5-89e8-542b77fdae85.png
.. |4| image:: https://cloud.githubusercontent.com/assets/209663/9546177/f500361e-4da9-11e5-9431-b2f42b90ca2f.png
