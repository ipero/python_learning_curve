try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Automated Testing',
    'author': 'Roman',
    'url': 'https://github.com/ipero/python_learning_curve/tree/master/python_the_hard_way',
    'download_url': 'https://github.com/ipero/python_learning_curve/tree/master/python_the_hard_way',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
