django-flat-theme
=================

Description
-----------

**django-flat-theme** brings fresh air to the default Django Admin
interface which hasn't changed 10 years from the very first version of
Django framework. This theme just makes UI modern and clean.

This app overrides default admin's CSS. All changes are about colors,
margins, sizes and icons. Nothing major.

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

Works correct in Django 1.5+.

Font
~~~~

This theme uses `Roboto <http://www.google.com/fonts/specimen/Roboto>`__
font which is under Apache 2.0 licence.

Testing
~~~~~~~

Tested in:

- IE7+ (IE8 and less doesn't support SVG so there are no icons displayed)
- FF30+ (Windows, Ubuntu, OSX)
- Chrome 35+ (Windows, Ubuntu, OSX)
- Safari 8 (OSX)

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
