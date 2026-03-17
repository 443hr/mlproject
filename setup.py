from setuptools import setup, find_packages

from typing import List

hypen_dot = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements from a file and returns them as a list."""
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hypen_dot in requirements:
            requirements.remove(hypen_dot)

    return requirements


setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    description='A sample Python package',
    author = 'Kushagra Singh',
    install_requires = get_requirements('requirements.txt')
    )
