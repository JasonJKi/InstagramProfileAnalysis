# Setup script for tf_cnnvis

import io
from setuptools import setup, find_packages

with io.open('README.md') as readme:
    long_description = ''.join(
        filter(lambda x: 'https://veripad.co/' not in x,
               readme.readlines()))

with open('README.md') as f:
    long_description = f.read()

dependencies = ['bs4 ', 
                'requests', 
                'h5py', 
                'Pillow', 
                ]

setup(
    name = "InstaAnalyticTools",
    packages=find_packages('src'),
    package_dir = {'': 'src'},

    version = "0.0.1",
    
    author = "Jason Ki",
    author_email = "ki.jasonj@gmail.com",
    
    description = ("Tools for "),

    license = "MIT",
    keywords = "Instagram Analytics",
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience ::  Developers"
        "Topic :: Utilities",
        "Topic :: Computer Vision",
        "Topic :: Machine Learning",
        "Topic :: Scientific/Engineering :: Visualization",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: <3.6",
    ],
    
    install_requires=dependencies,
    
)
