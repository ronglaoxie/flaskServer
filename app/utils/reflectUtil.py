import sys

def getReflectClass(module_path,class_name):
    module_name = class_name[0].lower() + class_name[1:]
    module_file_path = module_path + '.' + module_name
    try:
        module_object = __import__(module_file_path, fromlist=True)
        module_class = getattr(module_object, class_name)
    except ImportError as e:
        print('can not find module %s' %(module_file_path))
        return None
    return module_class

def getReflectFunc(object, func):
    if hasattr(object, func):
        return getattr(object, func)
    else:
        return None
