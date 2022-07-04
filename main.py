import ifcopenshell
from ifcJSON.file_converters.ifcjson.ifc2json4 import IFC2JSON4
from flask import Flask, request
import os
import json
from minio import Minio
from minio.error import InvalidResponseError
import io




def myifc2json(bucket, object):

    # Авторизация в Minio
    minioClient = Minio('192.168.20.44:9000',
                     access_key='snabiev',
                     secret_key='miniochanges33',
                     secure=False
                     )

    ifc_file =minioClient.get_object(bucket_name=bucket, object_name=object) # Получение объекта из хранилища в виде потока
    new_file = ifcopenshell.file.from_string(ifc_file.read().decode('ascii'))  # Преобразование потока в файл, который может прочитать ifc2json


    json_data = IFC2JSON4(new_file).spf2Json()  # Преобразование файла ifc в json
    new_bucket = f"{bucket}_json"

    minioClient.make_bucket(new_bucket)
    minioClient.put_object(new_bucket, object, json_data)

    return 'OK'



app = Flask(__name__)

@app.route("/get_json", methods=["POST"])
def get_json():
    form_data = request.get_data(as_text=True)
    data_object = json.loads(form_data)
    bucket = data_object["bucket_name"]
    object = data_object["object_name"]

    output = myifc2json(bucket, object)

    return f"{output}"







if __name__ == "__main__":
    app.run(debug=True)