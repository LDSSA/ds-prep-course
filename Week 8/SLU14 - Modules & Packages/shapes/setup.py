import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shapes", 
    version="1.0.0",
    author="ldssa",
    author_email="ldssa@ldssa",
    description="modules that represent shapes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LDSSA/ds-prep-course",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
