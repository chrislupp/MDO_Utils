from setuptools import setup, find_packages

__package_name__ = "mdo_utils"
__package_version__ = "0.1.0"



setup(
    name=__package_name__,
    version=__package_version__,
    description=("Useful OpenMDAO components"),
    author="Christopher A. Lupp",
    author_email="christopherlupp@gmail.com",
    zip_safe=False,
    packages = find_packages()
)