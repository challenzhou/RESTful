#coding:utf8
from setuptools import setup

setup(name='RESTful_service',
      version='0.1',
      description='examine',
      url='https://github.com/challenzhou/RESTful.git',
      author='challenzhou',
      author_email='challenzhou@gmail.com',
      license='GNU',
      packages=['restful'],
      include_package_data=True,
      install_requires=['soaplib', 'lxml', 'pytz', 'twisted', 'suds'],
      zip_safe=False)
