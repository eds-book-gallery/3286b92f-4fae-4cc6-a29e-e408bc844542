from minio import Minio
from minio.error import S3Error


def upload_to_client(
    access_key,
    secret_key,
    bucket_name, 
    source_object,
    name_upload

    ):
    client = Minio(
        "play.min.io",
        access_key=access_key,
        secret_key=secret_key,
    )

    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
    else:
        print(f"Bucket {bucket_name} already exists")

    client.fput_object(
        bucket_name, name_upload, source_object,
    )
    print(
        f"'{source_object}' is successfully uploaded as "
        f"object '{name_upload}' to bucket '{bucket_name}'."
    )
