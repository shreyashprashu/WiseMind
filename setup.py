"""
This code defines a Python package called `WiseMind` and uses the `setuptools` module to specify package metadata and 
dependencies.

The `find_packages` function from `setuptools` is used to automatically discover and include all sub-packages and modules 
in the package.

The `get_requirements` function is a helper function that reads a list of package requirements from a file specified by the 
`file_path` parameter, removes any newline characters from each line, and returns the list of requirements. If the list 
contains the string "-e .", indicating a reference to the current directory, it is removed.

The `setup` function from `setuptools` is used to specify the package metadata, including the name, version, author, author 
email, and package dependencies. The `install_requires` parameter specifies the list of package requirements obtained from 
the `get_requirements` function.
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads a list of package requirements from a file specified by the `file_path` parameter, 
    removes any newline characters from each line, and returns the list of requirements. If the list 
    contains the string "-e .", indicating a reference to the current directory, it is removed.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="WiseMind",
    version="0.0.1",
    author="shreyash",
    author_email="shreyashprashu93@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
