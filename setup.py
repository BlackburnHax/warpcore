import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="warpcore",
    version="1.0.1",
    description="Streamlined multi-threaded process acceleration",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BlackburnHax/warpcore",
    author="Brandon Blackburn",
    author_email="contact@bhax.net",
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["warpcore"],
    include_package_data=True,
    install_requires=[],
)