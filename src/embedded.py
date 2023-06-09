from aadservice import AadService
from flask import abort
import json
import requests
import base64
from PIL import Image
import io


def obtener_report_por_id_user(db,id_user):
    with db.connection.cursor() as cursor:
        juegos = []
        #print(type(id))
        #print(id)
        #result = cursor.execute("""SELECT id,name,report,role,descripcion FROM reports_workspace WHERE id_user = '{}'""".format(id_user))
        result = cursor.execute("""SELECT id,name,report,role,descripcion,name_img FROM reports_workspace WHERE id_user = %s""", (id_user,))
        juegos = cursor.fetchall()

        #imagen



    return juegos


def obtener_report_por_id_user2(db,id_repor):
    with db.connection.cursor() as cursor:
        juegos = []
        #print(type(id))
        #print(id)
        result = cursor.execute("""SELECT id,name,report,role,descripcion FROM reports_workspace WHERE id = %s""", (id_repor,))
        #result = cursor.execute("SELECT id,name,report,role,descripcion FROM reports_workspace WHERE id = '{}'""".format(id_repor))
        juegos = cursor.fetchone()
        #print(juegos)
    return juegos


def all_workshop2(app,db,id):
    url='https://api.powerbi.com/v1.0/myorg/groups'
    api_response = requests.get(url, headers=get_request_header(app,db,id))
    if api_response.status_code != 200:
        abort(api_response.status_code, description=f'Error while retrieving Embed URL\n{api_response.reason}:\t{api_response.text}\nRequestId:\t{api_response.headers.get("RequestId")}')
    api_response = json.loads(api_response.text)
    #print(api_response)
    api_response['value']

    return (api_response['value'])


def all_reports(app,db,workshop,id):
    reportes=[]
    # print(session)
    # print(workshop)
    for i in workshop:
        if i['type'] == 'Workspace':
            url=f"https://api.powerbi.com/v1.0/myorg/groups/{i['id']}/reports"
            api_response = requests.get(url, headers=get_request_header(app,db,id))
        # extra codigo por el error UnboundLocalError: cannot access local variable 'api_response'
        if api_response is None:
            return []
        #------------------------------------------
    if api_response.status_code != 200:
        abort(api_response.status_code, description=f'Error while retrieving Embed URL\n{api_response.reason}:\t{api_response.text}\nRequestId:\t{api_response.headers.get("RequestId")}')
    api_response = json.loads(api_response.text)
    print(api_response['value'])
    for a in api_response['value']:
        dic2={'id_workshop':i['id'],'id_report':a['id'], 'name_report':a['name'] }
        reportes.append(dic2)
    return (reportes)



def get_request_header():
        '''Get Power BI API request header

        Returns:
            Dict: Request header
        '''

        return {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + AadService.get_access_token()}