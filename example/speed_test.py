import os

from file_host_uploader.synchronous import gofile
from urllib.request import urlretrieve


def download_large_file(size=100000000, file_path="./"):
    file_name = f"{file_path}{100000000}.bin"
    if not os.path.exists(file_name):
        urlretrieve(url=f"https://speed.cloudflare.com/__down?bytes={size}", filename=file_name)
    else:
        print("file already downloaded")
    return file_name


def generale_large_file(size=1024 * 1024 * 1024, file_path="./"):
    file_name = f"{file_path}{size}.bin"
    if not os.path.exists(file_name):
        with open(file_name, "wb+") as out:
            out.seek(size - 1)
            out.write(b'\0')
    else:
        print("file already exist")
    return file_name


if __name__ == "__main__":
    # download_large_file()
    generale_large_file()
    print(gofile.upload_file("./white.png"))
