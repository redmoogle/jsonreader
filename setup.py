import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name='guildreader',
    version='2.0.2',
    author='Redmoogle',
    author_email='dakotamew@gmail.com',
    description='JSON Data Management Module',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/redmoogle/jsonreader',
    packages=setuptools.find_packages(),
    install_requires=[
        'ujson'
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.5'
)
