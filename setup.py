from setuptools import setup

dependencies = ['ipython']
extra-Packages = {'testing': ['pytest', 'pytest-watch']}

setup(
    name='codewars',
    description='Bunch of different functions',
    version='0.1',
    author=['JamesT', 'ErikE'],
    #author_email='',
    #license='',
    py_modules=['codewars'],
    #package_dir={'': 'src'}
    install_requires=dependencies,
    extra_require=extra_packages

)