"""
Based on https://gofile.io/api as of 2022-07-19
TODO: add support for using account
"""
import json
from io import BufferedReader
from typing import Union

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from util.exception import ParameterUnfulfilled, PreUploadError, MidUploadError, UploadError


def get_upload_server_name(session: requests.Session = requests.Session()):
    try:
        resp = session.get("https://api.gofile.io/getServer")
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    if resp.status_code != 200:
        print(f"status code: {resp.status_code}  {resp.text}")
        return None
    parsed_resp = resp.json()
    print(json.dumps(parsed_resp))
    if parsed_resp["status"] != "ok":
        print(f"status not ok: {parsed_resp['status']}")
        return None
    return parsed_resp["data"]["server"]


def make_upload_url(retry: int = 3, session: requests.Session = requests.Session()):
    upload_server_name = None
    for _ in range(retry):
        upload_server_name = get_upload_server_name(session=session)
        if upload_server_name:
            break
        else:
            print("failed to get upload server, retrying...")
    if not upload_server_name:
        raise PreUploadError("failed to get upload server")
    return f"https://{upload_server_name}.gofile.io/uploadFile"


def upload_file(file: Union[bytes, str], file_name: str = None, session: requests.Session = requests.Session()):
    """
    :param file:
    :param file_name:
    :param session:
    :return:

    If the file is in bytes, then it means it's small enough to fit in the memory
    Otherwise will be treated as a large file
    """
    if file_name is None:
        if isinstance(file, bytes):
            raise ParameterUnfulfilled("you need to also provide a file name if you provided the file in bytes")
        elif isinstance(file, str):
            file_name = file.split("/")[-1]
    url = make_upload_url(session=session)
    try:
        # resp = session.post(url, files={"file": (file_name, open(file, "rb").read())})
        if isinstance(file, str):
            actual_file = open(file, "rb")
        elif isinstance(file, bytes):
            actual_file = file
        else:
            raise TypeError("file must be a string or bytes")
        form = MultipartEncoder({"file": (file_name, actual_file)})
        header = {"Content-Type": form.content_type}
        resp = session.post(url=url, headers=header, data=form)  # ignore the error it will work anyway
        if isinstance(actual_file, BufferedReader):
            print(f"closing file handle for {file_name}")
            actual_file.close()
    except TypeError:
        raise PreUploadError("file must be a string or bytes")
    except requests.exceptions.RequestException as e:
        print(e)
        raise MidUploadError(f"failed to upload {file_name}")
    if resp.status_code != 200:
        raise UploadError(f"status code: {resp.status_code}  {resp.text}")
    parsed_resp = resp.json()
    if parsed_resp["status"] != "ok":
        raise UploadError(f"status not ok: {parsed_resp['status']}")
    return parsed_resp["data"]["downloadPage"]


if __name__ == "__main__":
    requests_session = requests.Session()
    # print(get_upload_server_name(session=requests_session))
    # print(make_upload_url(session=requests_session))
    print(upload_file(file="../example_file/blank_white.png",
                      session=requests_session))
    print(upload_file(file=open("../example_file/blank_white.png", "rb").read(),
                      file_name="blank_white.png",
                      session=requests_session))
