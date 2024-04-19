import os
import json
import requests
import xmltodict

soap_response_json = {}

url_soap = os.environ['url_soap']
options = {"Content-Type": "text/xml;charset=utf-8"}


def lambda_handler(event, context):
    try:
        if event['operacion'] is None:
            return json.dumps({'statusCode': 400, 'errors': "No se proporcionó el campo oprecion."})

        match event['operacion']:
            case "consultaHCAciertaQuantoDecisorV2":
                return consulta_hca_cierta_quanto_decisor_v2(event)
            case "consultaHCAciertaQuantoV2":
                return consulta_hca_cierta_quanto_v2(event)
            case "consultarFechaHora":
                return consultar_fecha_hora()
            case "":
                return json.dumps({'statusCode': 400, 'errors': "Null body"})
    except TypeError as e:
        return json.dumps({'statusCode': 500, 'errors': str(e)})
    except Exception as e:
        return json.dumps({'statusCode': 400, 'errors': str(e)})


def consulta_hca_cierta_quanto_decisor_v2(json_request) -> dict:
    soap_schema = build_schema_consulta_hca_cierta_quanto_decisor_v2(json_request['data'])
    response = requests.post(url_soap, data=soap_schema, headers=options)
    xml_to_json = xmltodict.parse(response.text)
    soap_response_json["statusCode"] = response.status_code.numerator
    soap_response_json["data"] = xml_to_json["S:Envelope"]["S:Body"]["ns2:consultaHCAciertaQuantoDecisorV2Response"]["return"]
    return soap_response_json


def consulta_hca_cierta_quanto_v2(json_request) -> dict:
    soap_schema = build_schema_consulta_hca_cierta_quanto_v2(json_request['data'])
    response = requests.post(url_soap, data=soap_schema, headers=options)
    xml_to_json = xmltodict.parse(response.text)
    soap_response_json["statusCode"] = response.status_code.numerator
    soap_response_json["data"] = xml_to_json["S:Envelope"]["S:Body"]["ns2:consultaHCAciertaQuantoV2Response"]["return"]
    return soap_response_json


def consultar_fecha_hora() -> dict:
    soap_schema = build_schema_consultar_fecha_hora()
    response = requests.post(url_soap, data=soap_schema, headers=options)
    xml_to_json = xmltodict.parse(response.text)
    soap_response_json["statusCode"] = response.status_code.numerator
    soap_response_json["data"] = xml_to_json["S:Envelope"]["S:Body"]["ns2:consultarFechaHoraResponse"]["return"]
    return soap_response_json


def build_schema_consulta_hca_cierta_quanto_decisor_v2(data) -> str:
    with open('schemas/schema_consulta_hca_cierta_quanto_decisor_v2.xml', 'r') as file:
        schema_template = file.read().format(idenProceso=data['idenProceso'], idenUsuario=data['idenUsuario'], nombreUsuario=data['nombreUsuario'], nroIdentificacion=data['nroIdentificacion'], origenConsulta=data['origenConsulta'], paramFormulario=data['paramFormulario'], primerApellido=data['primerApellido'], tipoDocumento=data['tipoDocumento'], usuario=data['usuario'])
    print(schema_template)
    return schema_template


def build_schema_consulta_hca_cierta_quanto_v2(data) -> str:
    with open('schemas/schema_consulta_hca_cierta_quanto_v2.xml', 'r') as file:
        schema_template = file.read().format(idenProceso=data['idenProceso'], idenUsuario=data['idenUsuario'], nombreUsuario=data['nombreUsuario'], nroIdentificacion=data['nroIdentificacion'], origenConsulta=data['origenConsulta'], primerApellido=data['primerApellido'], tipoDocumento=data['tipoDocumento'], usuario=data['usuario'])
    print(schema_template)
    return schema_template


def build_schema_consultar_fecha_hora() -> str:
    with open('schemas/schema_consultar_fecha_hora.xml', 'r') as file:
        schema = file.read()
    print(schema)
    return schema

