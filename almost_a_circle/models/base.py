#!/usr/bin/pythom3
import json
"""This is the base module"""


class Base:
    """This is the Base class of the module"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            with open(f"{cls.__name__}.json", mode='w', encoding="UTF8") as f:
                f.write("[]")
        else:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            json_str = json.dumps(obj_list)
            with open(f"{cls.__name__}.json", mode='w', encoding='UTF8') as f:
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with all attributes set based on
        provided dictionary
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                json_str = f.read()
                dat = json.loads(json_str)
                return [cls.create(**item) for item in dat]
        except FileNotFoundError:
            return []
