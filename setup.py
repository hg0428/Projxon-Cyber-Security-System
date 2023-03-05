import setuptools



with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Projxon Cyber Security System",                     # This is the name of the package
    version="0.0.2",                        # The initial release version
    author="Hudson Gouge",                     # Full name of the author
    description="A fast and unbreakable encrytion system.",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        'Development Status :: 5 - Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.7',                # Minimum version requirement of the package
    py_modules=["PCSS"],             # Name of the python package
    package_dir={'':'PCSS'},     # Directory of the source code of the package
    install_requires=[
        'bitarray',
        'passlib',
        'uuid',
        'hashlib',
    ]
)
