from setuptools import find_packages, setup

from typing import List

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPEN_DOT = "-e ."
def get_requirements() -> List[str]:
    
    with open(REQUIREMENTS_FILE_NAME, "r") as fptr:
        requirements = fptr.readlines()
        requirements = [r.replace("\n", "") for r in requirements if r != HYPEN_DOT]
        print(requirements)
        return requirements


setup(
    name="sensor",
    version="0.0.1",
    author="Subramanyam Sista",
    author_email="subramanyam.sista@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)