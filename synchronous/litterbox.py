import requests

if __name__ == "__main__":
    url = "https://litterbox.catbox.moe/resources/internals/api.php"

    payload = {'time': '1h',
               'reqtype': 'fileupload'}
    files = {
        'fileToUpload': ('blank_white.png', open("../example_file/blank_white.png", 'rb'), 'image/png')
    }

    headers = {
        'Cookie': 'PHPSESSID=hfppk8pkpusimeb9dlrgjbm8ve'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.status_code)
    print(response.text)
