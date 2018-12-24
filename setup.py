import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="marketing-email",
    version = "0.0.1",
    description = "Customizable HTML emails for Marketing Campaigns",
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/shravankumar9892/marketing-email.git",
    author="Shravankumar Balakrishna Shetty",
    author_email="shravankumarshetty9892@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
	"Programming Language :: Python",
    ],
    packages=["mail"],
    include_package_data=True,
    install_requires=["smptlib", "ssl", "email", "getpass"],
)
