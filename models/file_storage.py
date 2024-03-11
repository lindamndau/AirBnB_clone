#!/usr/bin/python3
""" Class FileStorage serilizes and desterializes instance, JSON file"""
class FileStorage:
    """ FileStorage class defined """
    def __init__(self,__file_path=None, __objects={}):
        self.__file_path = __file_path
        self.__objects = __objects

    @instance_method
    def all(self):
        return self.__objects

    @instance_method
    def new(self, obj):
        class_name = obj.__class__.name__
        obj_id = getattr(obj, 'id', None)
        if obj_id is None:
            raise ValueError("Object must have 'id' attribute.")
        key = f"{class_name}.{obj_id}"
        self.__objects[key] = obj
    
    @method
    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f, default=lambda o: o.__dict__)

    @method
    def reload(self):
        with open(self.__file_path, 'w') as f:
            if isinstance is __file_path:
               self.__objects = json.load(f)
            else:
                None
