from setuptools import setup, find_packages

def read_readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name='KrikNN',
    version='0.1',
    description='KrikNN is a library that includes various components for neural network operations and tensor manipulations. This README provides an overview of the `Tensor` class and its functionality, as well as instructions for running the tests.',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='Andrew Krikorian',
    url='https://github.com/andykr1k/kriknn',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    project_urls={
        'Bug Reports': 'https://github.com/andykr1k/kriknn/issues',
        'Source': 'https://github.com/andykr1k/kriknn',
    },
)
