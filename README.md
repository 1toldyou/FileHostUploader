# FileHostUploader
Utilize their API for direct upload


## Sync and Async
Whether you are creating a simple script or performance-drive application, 
we offer adapters with both [requests](https://pypi.org/project/requests/) and or [aiohttp](https://pypi.org/project/aiohttp/)

## Setup
for development

        python -m pip install requirements.txt

## Install
This package not being published to PyPI yet, 
so please don't run `pip install file_host_uploader`

### From Source
We do recommend you install this package in `venv` as it's still in beta,
and it might want to install some dependencies that conflict with other packages

        python -m pip install git+https://github.com/1toldyou/FileHostUploader.git
abd add the following to your `requirements.txt`

        git+https://github.com/1toldyou/FileHostUploader.git #egg=file_host_uploader
