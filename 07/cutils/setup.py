from setuptools import setup, Extension

setup(
    name = 'cutils',
    version = '1.0',
    description = 'C Extension for matrix operations',
    author = 'Bykov Vladimir',

    ext_modules = [
        Extension('cutils', ['cutils.c'])
    ]
)