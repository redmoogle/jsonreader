import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name='jsonreader',
    version='1.0.0',
    author='Redmoogle',
    author_email='dakotamew@gmail.com',
    description='DiscordPy Guild Data Management Module',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/redmoogle/jsonreader',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU V3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    python_requires='>=3.5'
)
