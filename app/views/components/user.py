import os
from app.views.baseComponent import BaseComponent
import json
class User(BaseComponent):
    def __init__(self, config):
        BaseComponent.__init__(self, config)

    def add(self):
        content = json.dumps({"error_code":"add"})
        resp = self.Response_headers(content)
        return resp

    def edit(self):
        content = json.dumps({"error_code":"edit"})
        resp = self.Response_headers(content)
        return resp

    def delete(self):
        pass

    def getList(self):
        pass

    def help(self):
        pass