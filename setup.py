#How to install matyautil
#pip install -e ./.                                                                                                                                  

from setuptools import setup, find_packages

setup(
    name='matyautil',
    version='0.1.0',
    license='none',
    description='python utils by matyalatte',

    author='Matyalatte',
    author_email='matyalatte@gmail.com',
    url='https://github.com/matyalatte/python_util',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=["numpy", "matplotlib"],
    extras_require={},

    entry_points={},
)