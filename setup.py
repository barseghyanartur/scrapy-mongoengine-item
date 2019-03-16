from setuptools import setup, find_packages


setup(
    name='scrapy-mongoengine-item',
    version='0.1.4',
    url='https://github.com/barseghyanartur/scrapy-mongoitem',
    description='Scrapy extension to write scraped items using MongoEngine '
                'documents',
    long_description=open('README.rst').read(),
    author='Artur Barseghyan',
    author_email='artur.barseghyan@gmail.com',
    license='GPL 2.0/LGPL 2.1',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Scrapy',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or "
        "later (LGPLv2+)",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
        'Framework :: Scrapy',
    ],
    install_requires=['six'],
    requires=['scrapy (>=0.24.5)', 'mongoengine'],
)
