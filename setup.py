from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Special opportunities for the Karakalpak language'
LONG_DESCRIPTION = 'This package includes various classes and methods tailored for the Karakalpak language. Among them are Latin-Cyrillic converters and functionalities for expressing numbers in word form.'

# Setting up
setup(
    name="kaalin",
    version=VERSION,
    author="Turdıbek Jumabaev",
    author_email="<turdibekjumabaev05@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['karakalpak', 'language', 'python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)