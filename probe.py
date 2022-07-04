import io
import json
from urllib.request import urlopen
from minio import Minio
from convert import convert_ifc_to_full_json
import io
from for_storage import put_object


minioClient = Minio('192.168.20.44:9000',
                     access_key='snabiev',
                     secret_key='miniochanges33',
                     secure=False
                     )


# with io.BytesIO() as json_buf:
#     data_from_minio = minioClient.get_object('nabievtest', 'KVPU_OV.ifc')
#     json_buf.write(data_from_minio.read())
#     json_buf.seek(0)

#
# ifc_file = minioClient.get_object(bucket_name='nabievtest', object_name='KVPU_OV.ifc')  # Получение объекта из хранилища в виде потока
# print(convert_ifc_to_full_json(ifc_file))



#     print(data_from_minio.read())
data = open('KVPU_OV.ifc', 'rb')
# json_data = json.dumps(convert_ifc_to_full_json(data))
# json_data_bytes = (json_data.encode())
# json_data_bytes_io = io.BytesIO(json_data_bytes)
put_object(bucket='nabievtest', project_id='1111', file_name="KVPU_OV.ifc", json_data=data)

# minioClient.make_bucket(new_bucket, "ru-spb-1")
# result = minioClient.put_object('nabievtestjson', "KVPU_OVjsonfile.json", json_data_bytes_io, length=-1, part_size= 1000*1024*1024)
# result = put_object(bucket='nabievtest', project_id='1111', file_name="KVPU_OVjsonfile.json", json_data=json_data_bytes_io)


# name = "KVPU_OV.ifc"
# print(name[:-3] + 'json')