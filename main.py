import ifcJSON
# from ifcJSON.file_converters import ifcjson
# import os
# import ifcopenshell
# import json
# from minio import Minio
# from minio.error import InvalidResponseError

# minioClient = Minio('192.168.20.44:9000',
#                  access_key='snabiev',
#                  secret_key='miniochanges33',
#                  secure=False
#                  )
#
# # file_path = os.path.abspath('')
# # minioClient.fget_object('nabievtest', 'OPU.ifc', 'OPU.ifc')
#
# file_name = 'OPU.ifc'
# # ifc_file = minioClient.fget_object(bucket_name='nabievtest',
# #                                    object_name=file_name,
# #                                    file_path=file_name)
#
# ifc_file =minioClient.get_object(bucket_name='nabievtest', object_name=file_name)
# new_file = ifcopenshell.file.from_string(ifc_file.read().decode('ascii'))
# print(new_file)


new_file = open('KVPU_OV.ifc')
k = ifcJSON.file_converters.ifcjson.IFC2JSON4(new_file).spf2Json()



# open_file = ifcopenshell.open(new_file)
# products = new_file.by_type('IfcProduct')
# for product in products:
#     print(product.is_a())


# jsonData = ifcjson.IFC2JSON4(new_file).spf2Json()
#
# print(jsonData)
