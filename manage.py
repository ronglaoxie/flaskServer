#coding:utf-8
import os
import sys
import json
from flask_script import Manager, Server

sys.path.append(os.getcwd())
from app import create_app


if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')

manager = Manager(app)
manager.add_command("runserver", Server(
    host = '0.0.0.0')
)
if __name__ == '__main__':
    manager.run()