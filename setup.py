from setuptools import setup


def desc():
    with open("README.md") as f:
        return f.read()


setup(
    name='frasco-search',
    version='0.1',
    url='http://github.com/frascoweb/frasco-search',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="Elastisearch integration for Frasco",
    long_description=desc(),
    py_modules=['frasco_search'],
    platforms='any',
    install_requires=[
        'frasco',
        'elasticsearch==1.2.0'
    ]
)