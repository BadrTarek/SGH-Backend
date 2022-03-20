import os
from urllib import response
import socketio
from Library.api_response import ApiResponse
from rest_framework import status
from Apps.Hardware.serializers import SensorValueSerializer, SensorSerializer, ActuatorSerializer, StoreSensorValuesSerializer, TakeActionSerializer, ActuatorActionsSerializer
from Apps.Greenhouses.serializers import GreenhouseSerializers, GreenhouseAuthSerializer
from Library.api_response import ApiResponse
from socketio.exceptions import ConnectionRefusedError
from FuzzyLogic import PHFuzzyLogic, TempFuzzyLogic

import timeit


def implement_fuzzy(ph, water_level, temp, temperature_rate):
    ph = PHFuzzyLogic(ph, water_level)
    temp = TempFuzzyLogic(temp, temperature_rate)

    if not temp.fuzzification():
        print("Error on temperature fuzzification process")
        return False
    elif not temp.apply_rules():
        print("Error on appling temperature rules process")
        return False
    elif not temp.defuzzification():
        print("Error on temperature defuzzification process")
        return False
    elif not ph.fuzzification():
        print("Error on PH fuzzification process")
        return False
    elif not ph.apply_rules():
        print("Error on PH appling rules process")
        return False
    elif not ph.defuzzification():
        print("Error on PH defuzzification process")
        return False
    else:
        print(f"PH pump value =  {ph.get_ph_pump_value()}")
        print(f"PH Alkaline value =  {ph.get_alkaline_pump_value()}")
        print(f"Fan speed value =  {temp.get_fan_speed_value()}")

        return {
            "ph_pump": ph.get_ph_pump_value(),
            "alkaline_pump": ph.get_alkaline_pump_value(),
            "fan": temp.get_fan_speed_value()
        }


# ------------------------------------------------------ Hardware Client
class HardwareNamespace(socketio.Namespace):

    def on_connect(self, sid, message):

        print("Hardware Connected Successfully")

        # serializer = GreenhouseAuthSerializer(data = message )

        # if not serializer.is_valid():
        #     api_response = ApiResponse()
        #     auth_field = api_response.set_status_code(400).set_data('errors',serializer.errors).get()
        #     raise ConnectionRefusedError(auth_field)

        # greenhouse , token = serializer.login()

        clients_response = ApiResponse()
        hardware_response = ApiResponse()

        response = clients_response.set_status_code(200).set_data(
            'message', 'Hardware connected successfully').get()

        self.enter_room(sid, namespace='/hardware',  room="myGreenhouse")
        self.emit('connection_status', hardware_response.set_data(
            'message', "Connected to server successfully").get(), namespace='/hardware', room="myGreenhouse")
        self.emit('hardware_connection', response,
                  namespace='/web',  room="myGreenhouse")
        self.emit('hardware_connection', response,
                  namespace='/mobile', room="myGreenhouse")

    def on_sensors_values(self, sid, data):
        print("Hardware Sent Sensor Values Successfully")

        api_response = ApiResponse()

        serializer = StoreSensorValuesSerializer(data=data)

        if not serializer.is_valid():
            print(serializer.errors)
            response = api_response.set_status_code(
                status.HTTP_400_BAD_REQUEST).set_data("errors", serializer.errors).get()
            self.emit('send_sensor_values_status', response,
                      namespace='/hardware', room="myGreenhouse")

        else:
            print("Successfully ya mega")
            sensor_values = serializer.save()
            api_response.set_status_code(status.HTTP_200_OK).set_data(
                "sensors", SensorValueSerializer(sensor_values, many=True).data)

            response = api_response.get()

        # response = "Sensor Values from NodeMCU"
        self.emit('sensors_values', response,
                  namespace='/web',  room='myGreenhouse')
        self.emit('sensors_values', response,
                  namespace='/mobile',  room='myGreenhouse')

    def on_disconnect(self, sid):
        print("Hardware Disconnected")

        api_response = ApiResponse()

        response = api_response.set_status_code(status.HTTP_501_NOT_IMPLEMENTED).set_data(
            'message', 'Hardware disconnected').get()

        self.emit('hardware_connection', response,
                  namespace='/web',  room='myGreenhouse')
        self.emit('hardware_connection', response,
                  namespace='/mobile',  room='myGreenhouse')


# print(
#     f"Execution time is: {timeit.timeit( stmt = HardwareNamespace.on_sensors_values, number = 1)}")
