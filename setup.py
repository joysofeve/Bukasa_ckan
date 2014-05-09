from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='bukassa_geonode',
    version=version,
    description="Theme for Drupal and Ckan",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Eve & Reinier',
    author_email='eve.ndagire@mountbatten.net',
    url='www.data.ug',
    license='GPL 3.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.bukassa'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        bukassa_geonode=ckanext.bukassa.plugin:BukassaThemePlugin
        # Add plugins here, e.g.
        # myplugin=ckanext.bukassa.plugin:PluginClass
    ''',
)
