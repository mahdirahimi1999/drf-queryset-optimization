from pathlib import Path

from setuptools import setup

# Read the long description from README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="drf-queryset-optimization",  # Change the package name here
    version="0.1.1",
    author="Mahdi Rahimi",
    author_email="mahdi.rahimi95@gmail.com",
    description="A package for optimizing querysets in Django REST Framework views and viewsets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mahdirahimi1999/drf-queryset-optimization",
    packages=["drf_queryset_optimization"],  # Change the package name here
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
