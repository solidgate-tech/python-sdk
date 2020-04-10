import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="solidgate-card-sdk",
    version="0.0.1",
    author="SolidGate",
    author_email="info@solidgate.com",
    description="Python API SDK for SolidGate payment gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://solidgate.atlassian.net/wiki/spaces/API/overview",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests']
)
