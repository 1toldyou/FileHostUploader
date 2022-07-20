try:
    print("try to import setuptools")
    from setuptools import setup
except ModuleNotFoundError:
    print("setuptools not found, using distutils")
    from distutils.core import setup

setup(
    name="file_host_uploader",
    version="1.0.0",
    author="1toldyou",
    url="https://github.com/1toldyou/FileHostUploader",
    description="all-in-one tool to upload file to various free or low-cost file sharing platform",
    packages=[
        "file_host_uploader"
        # "file_host_uploader.util",
        # "file_host_uploader.synchronous"
    ],
    install_requires=[
        "requests",
        "aiohttp",
        "python-magic-bin",
        "b2sdk>=1.17.3,<2.0.0"
    ]
)
