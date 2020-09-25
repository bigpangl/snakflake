"""

Project:    snakflake
Author:     LanHao
Date:       2020/9/22
Python:     python3.6

"""

from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Build import cythonize

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

ext_modules = [
    Extension("*", ["./snakflake/*.pyx"]),
]

setup(
    name="snakflake",
    version="1.0",
    packages=find_packages(),
    ext_modules=cythonize(ext_modules, annotate=True),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="LH",
    author_email="bigpangl@163.com",
    classifiers=[
        'Programming Language :: Python :>= 3.6',
    ]
)
