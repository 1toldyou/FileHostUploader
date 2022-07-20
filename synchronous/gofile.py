"""
Based on https://gofile.io/api as of 2022-07-19
TODO: add support for using account
"""
import json
import requests

from util.exception import PreUploadError


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


if __name__ == "__main__":
    requests_session = requests.Session()
    print(get_upload_server_name(session=requests_session))
    print(make_upload_url(session=requests_session))
