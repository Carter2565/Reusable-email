from setuptools import find_packages, setup

setup(
    name='reusable.email',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[
      'cryptography',
      'requests',
      'aiohttp',
      'typing_extensions'
    ],
)