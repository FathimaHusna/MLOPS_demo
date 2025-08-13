from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function returns a list of requirements from the requirements.txt file.
    """
    requirement_lst : List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
       
    except FileNotFoundError:
        print("requirements.txt file not found. Returning an empty list.")
    return requirement_lst



setup(
    name='mlops_demo',
    version='0.0.1',
    author='Fathimahusna',
    install_requires=get_requirements(),
    packages=find_packages(),
   
)   
