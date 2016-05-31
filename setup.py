#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import re
import os
import sys


try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    readme = ''


package = 'tapioca_twitter'
requirements = [
    'tapioca-wrapper<2',
    'requests-oauthlib>=0.4.2',
]
test_requirements = [

]


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


# python setup.py register
if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version(package)}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print("  git push --tags")
    sys.exit()


setup(
    name='tapioca-twitter',
    version=get_version(package),
    description='Twitter API wrapper using tapioca',
    long_description=readme,
    author='Filipe Ximenes',
    author_email='filipeximenes@gmail.com',
    url='https://github.com/vintasoftware/tapioca-twitter',
    packages=[
        'tapioca_twitter',
    ],
    package_dir={'tapioca_twitter': 'tapioca_twitter'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='tapioca_twitter',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
