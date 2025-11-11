from setuptools import setup

setup(
    name="ft_package",
    version="0.0.1",
    author="nkarapet",
    author_email="nkarapet@42.fr",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nkarapet42/\
Python-for-Data-Science/tree/main/day00/ex09",
    license="MIT",
    packages=["ft_package"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
