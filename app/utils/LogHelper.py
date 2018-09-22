import os
import json
import logging
from config import *
from app.utils.times import now
from flask import current_app
from app.utils.LogType import *
def log(type,msg):
    helper=LogHelper()
    helper.writeLog(type,msg)
class LogHelper():
    def __init__(self):
        pass


    def writeLog(self,type='info',msg='some log'):
        if type==LogType.info:
            current_app.logger.info(msg)
        elif type==LogType.debug:
            current_app.logger.debug(msg)
        elif type==LogType.warning:
            current_app.logger.warning(msg)
        elif type==LogType.error:
            current_app.logger.error(msg)

