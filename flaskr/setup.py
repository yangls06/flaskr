from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    description='a simple blog post app based on Flask',
    packages=find_packages(),
    include_package_data=True,
    requires=[
        'flask'
    ]
)