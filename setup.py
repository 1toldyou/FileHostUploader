try:
    print("try to import setuptools")
    from setuptools import setup
except ModuleNotFoundError:
    print("setuptools not found, using distutils")
    from distutils.core import setup

setup(
    name="FileHostUploader",
    version="1.0.0",
    author="1toldyou",
    url="https://github.com/1toldyou/FileHostUploader",
    description="all-in-one tool to upload file to various free or low-cost file sharing platform",
    packages=["file_host_uploader"]
)
