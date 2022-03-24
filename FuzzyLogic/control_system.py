

# def implement_controller(controller):
#     try:
#         controller.fuzzification()
#         controller.apply_rules()
#         return controller
#     except:
#         return False
    
    


class ImplementFuzzy:
    
    def set_sensors_values(self , sensors:list):
        self.sensors = sensors

    def __get_sensor(self, id:int):
        for sensor in self.sensors:
            if sensor.id == id:
                return sensor
        return None
    
    