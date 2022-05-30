from typing import Union
import time

import requests
import magic


def _base_upload(file_name: str, file_body: bytes, file_type: str, expiration_time: str = "1h", cookie: str = "PHPSESSID=hfppk8pkpusimeb9dlrgjbm8ve"):
    url = "https://litterbox.catbox.moe/resources/internals/api.php"

    payload = {'time': expiration_time,
               'reqtype': 'fileupload'}
    files = {
        'fileToUpload': (file_name, file_body, file_type)
    }

    headers = {
        'Cookie': cookie
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.status_code)
    print(response.text)

    if response.status_code == 200:
        return response.text
    else:
        return None


def upload(file_name: str, file: Union[bytes, str], file_type: str = None, expiration_time: str = "1h"):
    if isinstance(file, bytes):
        file_body = file
    elif isinstance(file, str):
        file_body = open(file, "rb").read()
    else:
        raise FileNotFoundError("you need provide a file to upload")
    if file_type is None:
        file_type = magic.from_file(file, mime=True)
    if not (expiration_time == "1h" or expiration_time == "12h" or expiration_time == "24h" or expiration_time == "72h"):
        expiration_time = "12h"
    return _base_upload(file_name=file_name,
                        file_body=file_body,
                        file_type=file_type,
                        expiration_time=expiration_time,
                        cookie="PHPSESSID=hfppk8pkpusimeb9dlrgjbm8ve")


# TODO
def get_cookie():
    pass


if __name__ == "__main__":
    start_time = time.time()
    print(upload(file_name="blank_white.png", file="../example_file/blank_white.png"))
    print("%s seconds" % (time.time() - start_time))
