from setuptools import find_packages, setup

setup(
    name = 'django-flat-theme',
    packages = find_packages(),
    version = __import__('flat').__version__,
    author = 'Alex D',
    author_email = 'mail@elky.me',
    description = ('A flat theme for Django admin interface. Modern, fresh, simple.'),
    license = 'BSD',
    url = 'https://github.com/elky/django-flat-theme',
    download_url = 'https://github.com/elky/django-flat-theme/tarball/0.9.3',
    keywords = ['django', 'admin', 'theme', 'interface'],
    include_package_data = True,
)
