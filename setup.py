import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyZenHub",
    version="0.1.0",
    author="John Rofrano",
    author_email="rofrano@gmail.com",
    description="A Python 3 library to communicate with the ZenHub REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rofrano/PyZenHub",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
)
