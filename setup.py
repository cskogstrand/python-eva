""" Setup for python-eva """

from setuptools import setup

setup(
    name='eva',
    version='0.0.1',
    description='Read and change status of Eva devices through Eva High Level API.',
    long_description='A module for reading and changing status of '
    + 'Eva devices through Eva High Level API. Compatible '
    + 'with Python3.',
    url='http://github.com/cskogstrand/python-eva',
    author='Christer Skogstrand',
    author_email='cskogstrand@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Home Automation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='home automation eva',
    install_requires=['requests>=2.20.0'],
    packages=['eva'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'eva=eva.__main__:main',
        ]
    })
