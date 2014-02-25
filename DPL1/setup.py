import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="DPL1",
    version='0.0.2',
    author='Ardelean Vlad',
    description=("The Django learning program project - a site where the uses"
                 "can take tests, and the admins can maintain configurations"
                 "for these tests"
    ),
    url='https://github.com/vladiibine/dlp-assignment1',
    keywords="example tutorial django",
    packages=['DPL1', 'home'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: Free For Educational Use",
    ]
)