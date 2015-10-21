#!/usr/bin/env python3
import setuptools
from setuptools.command.test import test as TestCommand
import sys


# https://pytest.org/latest/goodpractises.html#integration-with-setuptools-test-commands
class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  # import here, cause outside the eggs aren't loaded
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


version = '4.0'
release = '4.0.4'

setuptools.setup(
    name='cnorm',
    version=release,
    url='https://code.google.com/p/cnorm/',
    license='GPLv3',
    author='Lionel Auroux',
    author_email='lionel.auroux@gmail.com',
    description='CNORM a C Front-end in Python',
    keywords=['parsing', 'grammar', 'C'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['pyrser'],
    packages=[
        'cnorm',
        'cnorm.parsing',
        'cnorm.passes',
    ],
    entry_points={
        'console_scripts': ['cnorm=cnorm.main:main']
    },
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
