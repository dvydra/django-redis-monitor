import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README'))
readme = f.read()
f.close()

setup(
    name='django-redis-monitor',
    version="1.0.0",
    description='Request per second / SQLop per second monitoring for Django, using Redis for storage',
    long_description=readme,
    author='Simon Willison',
    author_email='simon@simonwillison.net',
    url='http://github.com/dvydra/django-redis-monitor',
    packages = ['django_redis_monitor'],
    classifiers=[
        'Development Status :: 5 - Production',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)