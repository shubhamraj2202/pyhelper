"""Package Release"""
from __future__ import annotations

from setuptools import find_packages, setup

setup(
    name="pyhelper-misc",
    version="1.0.0",
    description="Python Library Containing Generic Utilities and Helper Functions",
    long_description=open("README.md").read(),
    author="Shubham Raj",
    author_email="shubhamraj2202@gmail.com",
    url="https://www.linkedin.com/in/shubhamraj2202/",
    packages=find_packages(include=["py_helper", "py_helper.*"]),
    install_requires=[],
    tests_require=["pytest"],
)
