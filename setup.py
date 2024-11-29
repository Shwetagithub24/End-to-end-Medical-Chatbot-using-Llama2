# to setup the folders as local packages so that we can import some methods/functionalities into another file
# or we get module  not found error 

from setuptools import find_packages,setup

setup(
    name='Medical Chatbot',
    version='0.0.0',
    author="Shwwetanjali Zarekar",
    author_email="shwetazarekar6@gmail.com",
    packages=find_packages(),  # find constructor file in each folder and considers that folder as local package

)