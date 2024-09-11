from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) ->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements: #-e . connects to the setup.py while installing the packges and we do not want that to come here so to remove it we are using this constant and removing it from the list this -e . automatically finds the setup.py and triggers the logic
            requirements.remove(HYPEN_E_DOT)
    return requirements

# Metadata information
setup(
    name='mlproject',
    version='0.0.1',
    author='Yash Chauhan',
    author_email='yashchauhan528@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
