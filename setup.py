from setuptools import setup, find_packages

setup(
    name='radix-format',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'openpyxl',
        'xlrd'
    ],
    author='Jonathan Narvaez',
    author_email='asmot54@gmail.com'
)
