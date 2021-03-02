import re
from os import path

from setuptools import setup, find_packages

requirements = [
    'aniso8601>=0.82',
    'Flask>=0.8',
    'six>=1.3.0',
    'pytz',
]

version_file = path.join(
    path.dirname(__file__),
    'flask_restful',
    '__version__.py'
)
with open(version_file, 'r') as fp:
    m = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        fp.read(),
        re.M
    )
    version = m.groups(1)[0]

setup(
    name='FastAPI-RESTful',
    version=version,
    url='https://www.github.com/yairsimantov20/fastapi-restful/',
    description='Simple framework for creating REST APIs in FastAPI',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Framework :: FastAPI',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=requirements,
)
