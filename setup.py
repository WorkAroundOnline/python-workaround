from setuptools import setup, find_packages

setup(
    name='workaround',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python bindings for the WorkAround API',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/WorkAroundOnline/python-workaround',
    author='Severin Ibarluzea',
    author_email='info@workaroundonline.com'
)
