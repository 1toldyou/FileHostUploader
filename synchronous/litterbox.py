import time
import requests


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


def upload():
    return _base_upload(file_name="blank_white.png",
                        file_body=open("../example_file/blank_white.png", 'rb').read(),
                        file_type="image/png",
                        expiration_time="1h",
                        cookie="PHPSESSID=hfppk8pkpusimeb9dlrgjbm8ve")


if __name__ == "__main__":
    start_time = time.time()
    print(upload())
    print("%s seconds" % (time.time() - start_time))
