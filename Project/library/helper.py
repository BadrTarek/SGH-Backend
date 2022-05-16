from typing import Any
from .api_response import ApiResponse
from rest_framework import status 


def project_server():
    return "http://127.0.0.1:8000/"


def print_error_in_console(request_name , error):
    print("\n" + "*" * 70 + request_name + "*" * 70 + "\n")
    print(error)
    print("\n" + "*" * 100 + "\n")
    

class ModelObjectsHelper:
    def __init__(self) -> None:
        self.__objects = []
    
    def set_object(self, object ) -> 'ModelObjectsHelper':
        self.__objects.append(object)
        return self
    
    def set_objects(self, objects ) -> 'ModelObjectsHelper':
        for object in objects:
            self.__objects.append(object)
        return self
    
    def get_object(self,id:int) :
        for object in self.__objects:
            # print(object.sensor)
            # print(id)
            # print("*"*10)
            if object.sensor.id == id:
                return object
        return None

