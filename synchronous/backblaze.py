import json

from b2sdk.v2 import InMemoryAccountInfo, B2Api

if __name__ == "__main__":
    TOKEN = json.load(open("../FHU.token.json", encoding="utf-8"))
    info = InMemoryAccountInfo()
    b2_api = B2Api(info)
    b2_api.authorize_account("production", TOKEN["b2"]["application_key_id"], TOKEN["b2"]["application_key"])

    bucket = b2_api.get_bucket_by_name(TOKEN["b2"]["bucket_name"])
    print(bucket.bucket_info)
    result = bucket.upload_local_file(local_file="../example_file/blank_white.png", file_name="example.png")
    print(result.file_info, result.file_name, result.id_)
    print("finished")
