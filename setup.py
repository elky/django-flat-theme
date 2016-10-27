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
    download_url = 'https://github.com/elky/django-flat-theme/tarball/1.1.4',
    keywords = ['django', 'admin', 'theme', 'interface'],
    include_package_data = True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
