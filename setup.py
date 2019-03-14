from setuptools import setup, find_packages


setup(
    name='scrapy-mongoitem',
    version='0.1',
    url='https://github.com/barseghyanartur/scrapy-mongoitem',
    description='Scrapy extension to write scraped items using Mongoengine '
                'documents',
    long_description=open('README.rst').read(),
    author='Artur Barseghyan',
    license='GPL 2.0/LGPL 2.1',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Scrapy',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
        'Framework :: Scrapy',
    ],
    install_requires=['six'],
    requires=['scrapy (>=0.24.5)', 'mongoengine'],
)
