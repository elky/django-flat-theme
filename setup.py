import os

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-flat-theme",
    version = __import__('flat').__version__,
    author = "elky",
    author_email = "mail@elky.me",
    description = ("A flat theme for Django admin interface. Modern, fresh, simple."),
    license = "BSD",
    url = "https://github.com/elky/django-flat-theme",
    packages = find_packages(),
    include_package_data = True,
    long_description = read('README.md'),
    zip_safe = False,
    classifiers = [
        "Development Status :: 3 - Alpha",
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
