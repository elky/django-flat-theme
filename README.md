# django-flat-theme

## Description

**django-flat-theme** brings fresh air to the default Django Admin interface which hasn't changed 10 years from the very first version of Django framework. This theme just makes UI modern and clean.

This app just overrides default admin's CSS. All changes are about colors, margins, sizes. Nothing major.

**No any markup changes**.

## Installation
Install via pip: ```pip install git+https://github.com/elky/django-flat-theme.git@master```


1. Put ```flat``` app in your *INSTALLED_APPS* **before** ```django.contrib.admin```:

    ```
INSTALLED_APPS = (
        ...
        'flat',
        'django.contrib.admin',
        ...
)
```

2. That's it.


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
![screenshot 2015-03-10 12 09 22](https://cloud.githubusercontent.com/assets/209663/6570553/69f33268-c71e-11e4-9ac6-48866199f5f5.png)


**Dashboard**
![screenshot 2015-03-10 12 08 18](https://cloud.githubusercontent.com/assets/209663/6570557/76b7d878-c71e-11e4-8f25-513a0170fbba.png)


**List of objects**
![screenshot 2015-03-10 12 08 32](https://cloud.githubusercontent.com/assets/209663/6570565/8cd90460-c71e-11e4-87da-70dc340c7a50.png)


**New object**
![screenshot 2015-03-10 12 08 55](https://cloud.githubusercontent.com/assets/209663/6570563/8074bc1e-c71e-11e4-97e4-146f9d824f81.png)
