from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(
    name='virtstrap-npm',
    version=version,
    description="A virtstrap plugin that installs node dependencies",
    long_description="""\
A virtstrap plugin that installs bundler's Gemfiles""",
    classifiers=[],
    keywords='virtstrap ruby bundler virtualenv pip',
    author='Reuven V. Gonzales',
    author_email='reuven@tobetter.us',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'virtstrap-local',
    ],
    entry_points={
        'virtstrap_local.plugins': [
            'npm = virtstrap_npm.plugin',
        ]
    },
)
