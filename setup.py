import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlpandas",
    version="0.0.1",
    author="Jean-Romain Roy",
    author_email="roy.jeanromain@gmail.com",
    description="SQL interface to a pandas dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeanromainroy/sqlpandas",
    packages=['sqlpandas'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: proprietary and confidential",
        "Operating System :: UNIX",
    ],
    install_requires=[
        'pandas',
        'click'
    ],
    python_requires='>=3.6',
)