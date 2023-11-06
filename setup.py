from setuptools import setup
import setuptools

setup(
    name= "mygenomic",
    description="Cet module permet de faire une transcriptiond'ADN en ARN",
    author="Sana Alidou Simande",
    packages=setuptools.find_packages(),
    entry_points= {"console_scripts":["my-genomic = genomic.genomic:run"]},
)   