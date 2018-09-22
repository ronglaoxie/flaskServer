import os
import json
import logging
from flask import request,make_response,Response
from config import *
from app.utils.times import now
from app.utils.mysqlHelper import *
from app.utils.LogHelper import *
from flask import current_app
class BaseComponent():
    def __init__(self,config):
        pass

    def add(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

    def getList(self):
        pass

    def help(self):
        print('Msg')



    #object to json
    def py_to_json(self,py_data):
        return json.dumps(py_data)
    #json to object
    def json_to_py(self,str):
        return json.loads(str)

    def writeLog(self,type='info',msg='some log'):
        if type=='log':
            current_app.logger.info(msg)
        elif type=='log':
            current_app.debug.info(msg)
        elif type=='log':
            current_app.warning.info(msg)
        elif type=='log':
            current_app.error.info(msg)

    def Response_headers(self,content):
        resp = Response(content)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp