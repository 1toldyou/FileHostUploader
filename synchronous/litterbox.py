from typing import Union
import time

import requests
import magic


def _base_upload(file_name: str, file_body: bytes, file_type: str, expiration_time: str, cookie: str, client: requests.Session):
    url = "https://litterbox.catbox.moe/resources/internals/api.php"

    payload = {'time': expiration_time, 'reqtype': 'fileupload'}
    files = {'fileToUpload': (file_name, file_body, file_type)}
    headers = {'Cookie': cookie}

    resp = requests.post(url, headers=headers, data=payload, files=files)
    print(resp.status_code)
    print(resp.text)

    if resp.status_code == 200:
        return resp.text
    else:
        return None


def upload(file_name: str, file: Union[bytes, str], file_type: str = None, expiration_time: str = "1h", cookie: str = "", client: requests.Session = requests.Session()):
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
                        cookie=cookie,
                        client=client)


def get_cookie(client: requests.Session = requests.Session()):
    resp = client.get("https://litterbox.catbox.moe/")
    if resp.status_code == 200:
        return f"PHPSESSID={list(resp.cookies.values())[0]}"
    else:
        return ""


if __name__ == "__main__":
    start_time = time.time()
    session = requests.Session()
    print(upload(file_name="blank_white.png",
                 file="../example_file/blank_white.png",
                 client=session,
                 cookie=get_cookie(client=session)))
    print("%s seconds" % (time.time() - start_time))
