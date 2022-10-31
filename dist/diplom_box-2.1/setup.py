from distutils.core import setup


setup(
    name='diplom_box',
    version='2.1',
    description='diplom module',
    author='zhenya',
    author_email='zhenya@gmail.com',
    packages=['full_scripts'],
    package_dir={'full_scripts': 'full_scripts'},
    package_data={'full_scripts': ['*.dat']},
)
