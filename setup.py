from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:

    requirements_list: List[str] = []
    return requirements_list


setup(
    name="Sensor",
    version="0.0.1",
    description="Sensor fault detection System",
    author="Deepanshu rajput",
    author_email="201812009@daiict.ac.in",
    packages=find_packages(),
    install_requires=[],
)
