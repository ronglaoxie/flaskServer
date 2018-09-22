#coding:utf-8
import json
from flask import Blueprint, request,make_response,Response
from flask_login import current_user
from flask import flash, redirect, url_for
from app.extensions import db
from app.utils.reflectUtil import *
from config import *
from app.utils.LogHelper import log
from app.utils.LogType import *
main = Blueprint('main', __name__)


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@main.route("/<module>/<cmd>", methods=['GET', 'POST'])
def index(module,cmd):
    log(LogType.info,'receive request,module:%s,commamd:%s;'%(module,cmd))
    if request.method == 'POST':
        # POST:
        # request.form获得所有post参数放在一个类似dict类中,to_dict()是字典化
        # 单个参数可以通过request.form.to_dict().get("xxx","")获得
        # ----------------------------------------------------
        # GET:
        # request.args获得所有get参数放在一个类似dict类中,to_dict()是字典化
        # 单个参数可以通过request.args.to_dict().get('xxx',"")获得
        datax = request.form.to_dict()
        content = str(datax)
        resp = Response_headers(content)
        moduleName = module[0].upper() + module[1:]
        module_class = getReflectClass('app.views.components', moduleName)
        if module_class is None:
            return 'can not execute, module:%s,cmd:%s' % (moduleName, cmd)
        class_object = module_class(config)
        class_func = getReflectFunc(class_object, cmd)
        if class_func:
            return class_func()
        else:
            return 'can not execute, module:%s,cmd:%s' % (moduleName, cmd)
    elif request.method == 'GET':
        content = json.dumps({"error_code":"1001"})
        resp = Response_headers(content)
        return resp
