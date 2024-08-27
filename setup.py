from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='KrikNN',
    version='0.1',
    description='KrikNN is a library that includes various components for neural network operations and tensor manipulations. This README provides an overview of the `Tensor` class and its functionality, as well as instructions for running the tests.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Andrew Krikorian',
    license='MIT',
    url='https://github.com/andykr1k/kriknn',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    project_urls={
        'Bug Reports': 'https://github.com/andykr1k/kriknn/issues',
        'Source': 'https://github.com/andykr1k/kriknn',
    },
)
