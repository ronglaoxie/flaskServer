#coding:utf-8
# 导入类库
from flask_sqlalchemy import SQLAlchemy
import logging
import time
import os
# 创建对象
db = SQLAlchemy()

# 初始化对象
def config_extensions(app):
    db.init_app(app)
    log_dir_name = "logs"
    log_file_name = 'logger-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    log_file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) + os.sep + log_dir_name
    make_dir(log_file_folder)
    log_file_str = log_file_folder + os.sep + log_file_name
    log_level = logging.WARNING

    handler = logging.FileHandler(log_file_str, encoding='UTF-8')
    handler.setLevel(log_level)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)

#log配置，实现日志自动按日期生成日志文件
def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path

