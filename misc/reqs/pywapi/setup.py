from distutils.core import setup

from pywapi import __version__


setup(name='pywapi',
    version=__version__,
    description='Python wrapper around different weather APIs',
    author='Eugene Kaznacheev, Joshua Tasker',
    author_email='qetzal@gmail.com, jtasker@gmail.com',
    url='http://code.google.com/p/python-weather-api/',
    py_modules=['pywapi'],
    license='MIT',
    keywords = 'weather api yahoo noaa google',
    platforms = 'any',
    long_description = """
This module provides a Python wrapper around the Yahoo! Weather, Weather.com,
and National Oceanic and Atmospheric Administration (NOAA) APIs. Fetch
weather reports using zip code, location id, city name, state, country, etc.
    """
)
