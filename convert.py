import ifcopenshell
import urllib3.response
from ifcJSON.file_converters.ifcjson.ifc2json4 import IFC2JSON4


def convert_ifc_to_full_json(ifc_file: urllib3.response.HTTPResponse) -> dict:
    """ convert entire ifc to json """

    decoded_file = ifcopenshell.file.from_string(
        ifc_file.read().decode('ascii'))  #TODO Преобразование потока в файл, который может прочитать ifc2json (Почему ascii?)
    json_data = IFC2JSON4(decoded_file).spf2Json()  # Преобразование файла ifc в json

    return json_data
