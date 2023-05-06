from minio_helper import upload_to_client

# Load raw data to MinIO Client

    try:
        upload_to_client(
            access_key,
            secret_key,
            bucket_name, 
            source_object,
            name_upload
            )
    except S3Error as exc:
        print("error occurred.", exc)