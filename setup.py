import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="projxon_cyber_security_system",  # This is the name of the package
  version="0.3.4",  # The release version
  author="Hudson Gouge",  # Full name of the author
  description="A fast and unbreakable encrytion system.",
  long_description=
  long_description,  # Long description read from the the readme file
  long_description_content_type="text/markdown",
  packages=setuptools.find_packages(
  ),  # List of all python modules to be installed
  download_url=
  'https://github.com/hg0428/Projxon-Cyber-Security-System/archive/refs/tags/stable-0.3.4.tar.gz',
  classifiers=[
    'Intended Audience :: Developers',  # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],  # Information to filter the project on PyPi website
  python_requires='>=3.7',  # Minimum version requirement of the package
  py_modules=["PCSS"],  # Name of the python package
  package_dir={'': '/home/runner/Projxon-Cyber-Security-System/'
               },  # Directory of the source code of the package
  install_requires=['bitarray', 'passlib', 'uuid'])
