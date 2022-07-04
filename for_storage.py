import urllib3.response
from minio import Minio
from config_data.config import ACCESS_KEY, SECRET_KEY, BUCKET_NAME
from typing import Any


def get_object(project_id: str, file_name: str) -> urllib3.response.HTTPResponse:
    """ Get file from storage """

    try:
        minio_client = Minio(endpoint='192.168.20.44:9000',
                             access_key=ACCESS_KEY,
                             secret_key=SECRET_KEY,
                             secure=False)

        if minio_client.bucket_exists(BUCKET_NAME):
            object_name = f'{project_id}/{file_name}'
            file = minio_client.get_object(bucket_name=BUCKET_NAME,
                                           object_name=object_name)
            return file
        else:
            raise Exception("Can't get file")
    except:
        raise Exception('Connection problem')


def put_object(project_id: str, file_name: str, json_data) -> bool:
    """ Put file to storage """

    try:
        minio_client = Minio(endpoint='192.168.20.44:9000',
                             access_key=ACCESS_KEY,
                             secret_key=SECRET_KEY,
                             secure=False
                             )

        if minio_client.bucket_exists(BUCKET_NAME):
            object_name = f'{project_id}/{file_name}'
            minio_client.put_object(bucket_name=BUCKET_NAME,
                                    object_name=object_name,
                                    data=json_data,
                                    length=-1,
                                    part_size=1000 * 1024 * 1024)
            return True
        else:
            raise Exception("No bucket")
    except:
        raise Exception("connection promblem")

# file = open('KVPU_OV.ifc', 'rb')
# put_object('nabievtest', '1111', file)
# k = get_object('1111', 'KVPU_OV.ifc')
# print(k)
