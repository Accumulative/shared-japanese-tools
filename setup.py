import setuptools
from setuptools.command.install import install


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='shared_japanese_tools',
    version='0.1',
    packages=['shared_japanese_tools'],
    author="Kieran Burke",
    author_email="kieranburke@live.com",
    description="A set of tools for learning japanese",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Accumulative/shared_japanese_tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
