from setuptools import setup,  find_packages 

setup(
    name='posetrack21eval', 
    version='0.1', 
    packages=find_packages(include=['evaluation_kit',  'evaluation_kit.*'])
)
