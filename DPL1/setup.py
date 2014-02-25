import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="DPL1",
    version='0.0.6',
    author='Ardelean Vlad',
    author_email="vlad.ardelean@3pillarglobal.com",
    description=("The Django learning program project - a site where the uses"
                 "can take tests, and the admins can maintain configurations"
                 "for these tests"
    ),
    url='https://github.com/vladiibine/dlp-assignment1',
    keywords="example tutorial django",
    packages=['DPL1', 'testing'],
    long_description=read('README.txt'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: Free For Educational Use",
    ],
    install_requires=["django==1.6.1", "south==0.8.4"]
)