from setuptools import setup, find_packages

setup(
    name="peptimizer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "rdkit",
        "textdistance"
    ],
)
