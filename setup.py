#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from codecs import open
from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

requirements = [
    "Click>=6.0",
    "colorama",
    "cookiecutter",
    "coverage",
    "pytest-runner",
    "pytest>=3.5.0",
    "setuptools>=30.0.0"
    "tox",
    "tutorial-runner>=0.2.7",
]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

dev_requirements = ["bumpversion", "flake8", "pip", "twine", "watchdog", "wheel"]

setup(
    author="Dave Forgac",
    author_email="tylerdave@tylerdave.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="A tutorial for writing command line applications using click.",
    entry_points={
        "console_scripts": [
            "pycon=click_tutorial.cli:main",
            "part01=lessons.part_01.cli:cli",
            "part02=lessons.part_02.cli:cli",
            "part03=lessons.part_03.cli:cli",
            "part05=lessons.part_05.cli:cli",
        ]
    },
    install_requires=requirements,
    license="Mozilla Public License 2.0 (MPL 2.0)",
    long_description=readme,
    include_package_data=True,
    keywords="click_tutorial",
    name="click_tutorial",
    packages=find_packages(include=["click_tutorial", "lessons"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    extras_require={"dev": dev_requirements},
    url="https://github.com/tylerdave/click_tutorial",
    version="1.0.2",
    zip_safe=False,
)
