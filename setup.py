from setuptools import setup, find_packages

setup(
    name='Ninjatrader_Data_Converter',
    version='0.1dev',
    author='Phil Rongo',
    packages=find_packages(),
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
    python_requires='>=3.6'
)