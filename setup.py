import os
import sys
from setuptools import setup, find_packages
from pprint import pprint

current_dir = os.getcwd()
deployable_dir = os.path.join(os.getcwd(), 'dpl1_main')
sys.path = list(set(sys.path))
sys.path.remove(current_dir)
sys.path.append(deployable_dir)

pprint("~~~VWH::: %s" % str(sys.path))


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#The files included as source files, that are build into a .tar.gz archive
# can be specified in the MANIFEST.in

#todo: check if
#The files included in the .egg archive must be found with find_packages() ?


found_packages = find_packages()
print "~~~VWH::: %s" % found_packages

setup(
    name="django-dlp-vgardelean-website1",
    version='0.0.2',
    author='Ardelean Vlad',
    author_email="vlad.ardelean@3pillarglobal.com",
    description=("The Django learning program project - a site where the uses"
                 "can take tests, and the admins can maintain configurations"
                 "for these tests"
    ),
    url='https://github.com/vladiibine/dlp-assignment1',
    keywords="example tutorial django",
    # packages=['DLP','DLP.DLP','DLP.testing_app'],
    #todo tell someone about this piece of crap so that they know!!!
    # package_dir={'': './dpl1_main'},
    packages=found_packages,
    package_data={'': ['*.html', '*.sqlite3', '*.json']},
    long_description=read('README.txt'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: Free For Educational Use",
    ],
    install_requires=["django==1.6.1", "south==0.8.4"],
    include_package_data=True
)
# pprint("~~~VWH::: %s" % str(sys.path))
