# django-flat-theme

## Description

**django-flat-theme** brings fresh air to the default Django Admin interface which hasn't changed 10 years from the very first version of Django framework. This theme just makes UI modern and clean.

This app just overrides default admin's CSS. All changes are about colors, margins, sizes. Nothing major.

**No any markup changes**.

## Installation
Install via pip: ```pip install git+https://github.com/elky/django-flat-theme.git@master```


1. Put ```flat``` app in your *INSTALLED_APPS* **BEFORE** ```django.contrib.admin```:

    ```
INSTALLED_APPS = (
        ...
        'flat',
        'django.contrib.admin',
        ...
)
```

That's it.


### Compatibility
Tested with Django 1.7 only. If you find any problems in other Django versions - please [create an issue](https://github.com/elky/django-flat-theme/issues/new).

### Font
This theme uses [Roboto](http://www.google.com/fonts/specimen/Roboto) font. It includes Latin, Latin Extended, Cyrilic, Cyrilic Extended, Greek, Greek Extended subsets. Not sure about others. I will appreciate if someone would test admin interface with **i18n** to find any font issues.

### Testing
Tested in:
- IE7+ (IE7 and IE8 are OK in terms of graceful degradation)
- FF30+ (Windows, Ubuntu, OSX)
- Chrome 35+ (Windows, Ubuntu, OSX)
- Safari 8 (OSX)

### Screenshot Examples

**Login page**
![screenshot 2015-03-10 2 23 58](https://cloud.githubusercontent.com/assets/209663/6565257/94e68806-c6d0-11e4-82e1-7db575c5da73.png)

**Dashboard**
![screenshot 2015-03-10 2 25 20](https://cloud.githubusercontent.com/assets/209663/6565267/a4140682-c6d0-11e4-92aa-8087bb3feb5a.png)

**List of objects**
![screenshot 2015-03-10 2 24 13](https://cloud.githubusercontent.com/assets/209663/6565271/aeee71fa-c6d0-11e4-9ab3-efec2fca49c5.png)

**New object**
![screenshot 2015-03-10 2 24 34](https://cloud.githubusercontent.com/assets/209663/6565288/ba0699c8-c6d0-11e4-9ec0-4171858376ed.png)


