import json

from b2sdk.v2 import InMemoryAccountInfo, B2Api

from util.math_helper import clamp


def _make_pre_signed_url(base_url: str, authorization: str):
    return f"{base_url}?Authorization={authorization}"


def make_pre_signed_url_by_filename(b2_api_client: B2Api, bucket_name: str, file_name: str, valid_duration: int):
    """
    :param b2_api_client:
    :param bucket_name:
    :param file_name:
    :param valid_duration:
    :return: pre-signed url
    """
    return _make_pre_signed_url(base_url=b2_api_client.
                                get_download_url_for_file_name(bucket_name, file_name),
                                authorization=b2_api_client.
                                get_bucket_by_name(bucket_name).
                                get_download_authorization(file_name, clamp(valid_duration, 0, 604800)))


if __name__ == "__main__":
    TOKEN = json.load(open("../FHU.token.json", encoding="utf-8"))
    info = InMemoryAccountInfo()
    b2_api = B2Api(info)
    b2_api.authorize_account("production", TOKEN["b2"]["application_key_id"], TOKEN["b2"]["application_key"])

    bucket = b2_api.get_bucket_by_name(TOKEN["b2"]["bucket_name"])
    print(bucket.bucket_info)  # returned an empty dict
    result = bucket.upload_local_file(local_file="../example_file/blank_white.png", file_name="example.png")
    print(result.file_name, result.id_)
    # print(b2_api.get_file_info(result.id_).as_dict())
    # print(b2_api.get_download_url_for_fileid(result.id_))
    # print(b2_api.get_download_url_for_file_name(TOKEN["b2"]["bucket_name"], result.file_name))
    # print(bucket.get_download_authorization(result.file_name, 3600))
    # print(bucket.get_download_authorization(result.file_name, 86400))
    # print(bucket.get_download_authorization(result.file_name, 604800))  # maximum
    print(make_pre_signed_url_by_filename(b2_api, TOKEN["b2"]["bucket_name"], result.file_name, 604800))
    print("finished")
