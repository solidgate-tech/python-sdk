import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="solidgate-sdk",
    version="0.2.1",
    author="SolidGate",
    author_email="info@solidgate.com",
    description="Python API SDK for SolidGate payment gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://api-docs.solidgate.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests', 'pycryptodome']
)
