import json
from flask import Flask, request
from for_storage import get_object, put_object
from convert import convert_ifc_to_full_json
import io


app = Flask(__name__)

@app.route("/get_json", methods=["POST"])
def get_json():

    form_data = request.get_data(as_text=True)
    data_object = json.loads(form_data)
    project_id: str = data_object["project_id"]
    object_name: str = data_object["object_name"]
    object = get_object(project_id, object_name)

    json_data_bytes: bytes = json.dumps(convert_ifc_to_full_json(object)).encode()
    json_data_bytes_io: io.BytesIO = io.BytesIO(json_data_bytes)

    json_object_name = object_name[:-3] + 'json'
    put_object(project_id, json_object_name, json_data_bytes_io)

    return 'OK'


if __name__ == "__main__":
    app.run(debug=True)