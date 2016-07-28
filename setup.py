import os

from static_import import __version__, __email__, __owner__, __license__
from setuptools import find_packages, setup

short_description = 'Add static files never was so easy.'
packages = find_packages()
package_data = { 'static_import': ['templates/*'] }

current_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_dir, 'README.md'), 'r') as f:
    readme = f.read()


setup(
    name='django_staticimport',
    version=__version__,
    url='https://github.com/leoxnidas/django_staticimport',
    license=__license__,
    description=short_description,
    long_description=readme,
    author=__owner__,
    author_email=__email__,
    packages=packages,
    package_data=package_data,
    install_requires=['Django >= 1.0'],
    keywords=['django', 'static_import', 'static files', 'static'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 0.0.1 - Production/Stable',
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
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
