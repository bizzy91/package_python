from setuptools import setup, find_packages

setup(
    name='bizzy_lib',
    version='0.0.1',
    description='pip test',
    author='bizzy',
    author_email='bizzybak@gmail.com',
    url='https://github.com/bizzy91/package_python.git',
    license="bizzy",
    packages=["bizzy_lib"],
    zip_safe=False,
    install_requires=[
        'numpy==1.18.3'
    ],
)
