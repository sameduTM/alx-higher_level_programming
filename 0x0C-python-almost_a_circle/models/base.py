#!/usr/bin/python3
"""This is the base module"""
import json
import csv


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
            json_str = cls.to_json_string(obj_list)
            with open(f"{cls.__name__}.json", mode='w', encoding='UTF8') as f:
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
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
                dat = cls.from_json_string(json_str)
                return [cls.create(**item) for item in dat]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a CSV file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x,
                                     obj.y])
            elif cls.__name__ == 'Square':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load data from a CSV file.

        Returns:
            list: A list containing instances of the class loaded
                from the CSV file.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                if cls.__name__ == "Rectangle":
                    return [cls.create(id=int(row[0]), width=int(row[1]),
                                       height=int(row[3]), x=int(row[4]),
                                       y=int(row[5])) for row in reader]
                elif cls.__name__ == "Square":
                    return [cls.create(id=int(row[0]), size=int(row[1]),
                                       x=int(row[2]),
                                       y=int(row[3])) for row in reader]
        except FileNotFoundError:
            return []
