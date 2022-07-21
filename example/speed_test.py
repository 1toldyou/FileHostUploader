import os
from datetime import datetime

from file_host_uploader.synchronous import gofile


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
    the_file = generale_large_file()
    gofile_start_time = datetime.now()
    print(gofile.upload_file(the_file))
    print(f"took {datetime.now() - gofile_start_time} to upload {the_file} to gofile.io")
