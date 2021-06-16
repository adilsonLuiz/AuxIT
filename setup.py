from sys import version
import setuptools

with open('README.md', 'r') as fl:
    content = fl.read()
    fl.close()


setuptools.setup(

    name = 'AuxI',
    version = '1.0',
    author = 'Adilson Luiz',
    description = 'Uma ferramenta para organização de arquivos, backup e instalação de programas',
    long_description = content,
    projects = {
        'Source': 'https://github.com/ShellAndPython/AuxIT'
    },
    install_requires = ['googledrivedownloader', 'requests'],
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    python_requires = '>=3.6'
)