import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class TempFuzzyLogic:    
    def __convert_to_fahrenheit(self,temp):
        return (float(temp) * 1.8) + 32
    
    def fuzzification(self):
        try:

            self.__temp_membership = ctrl.Antecedent(
                np.arange(0, 80, 0.1), "temperature")  # Unit is fahrenheit
            # Rate of change of temperature = (Previous Temperature – CurrentTemperature)
            self.__temp_rate_mambership = ctrl.Antecedent(
                np.arange(-50, 50, 1), "temperature_change_rate")
            self.__fan_membership = ctrl.Consequent(
                np.arange(0, 200, 1), "fan_speed")

            self.__temp_membership['cold'] = fuzz.trapmf(
                self.__temp_membership.universe, [0, 0, 50, 60])
            self.__temp_membership['normal'] = fuzz.trimf(
                self.__temp_membership.universe, [60, 62.5, 65])
            self.__temp_membership['hot'] = fuzz.trapmf(
                self.__temp_membership.universe, [65, 70, 80, 80])
            
            self.__temp_rate_mambership['cold'] = fuzz.trapmf(
                self.__temp_rate_mambership .universe, [-50,-50, -10, 0])
            self.__temp_rate_mambership['normal'] = fuzz.trimf(
                self.__temp_rate_mambership .universe, [-10, 0, 10])
            self.__temp_rate_mambership['hot'] = fuzz.trapmf(
                self.__temp_rate_mambership .universe, [0, 10, 50,50])

            self.__fan_membership['slow'] = fuzz.trapmf(
                self.__fan_membership.universe, [0, 0, 63, 127])
            self.__fan_membership['medium'] = fuzz.trimf(
                self.__fan_membership.universe, [63, 127, 191])
            self.__fan_membership['fast'] = fuzz.trapmf(
                self.__fan_membership.universe, [127, 191, 200, 200])

            return True
        except:
            print("Error in Temperature model in fuzzification process")
            return False

    def apply_rules(self):
        try:
            self.__rules = []
            self.__rules.append(ctrl.Rule(
                self.__temp_membership['cold'] & self.__temp_rate_mambership['cold'], self.__fan_membership['slow']))
            self.__rules.append(ctrl.Rule(
                self.__temp_membership['cold'] & self.__temp_rate_mambership['normal'], self.__fan_membership['medium']))
            self.__rules.append(ctrl.Rule(
                self.__temp_membership['cold'] & self.__temp_rate_mambership['hot'], self.__fan_membership['medium']))

            self.__rules.append(ctrl.Rule(
                self.__temp_membership['normal'] & self.__temp_rate_mambership['cold'], self.__fan_membership['medium']))
            self.__rules.append(ctrl.Rule(
                self.__temp_membership['normal'] & self.__temp_rate_mambership['normal'], self.__fan_membership['medium']))
            self.__rules.append(ctrl.Rule(
                self.__temp_membership['normal'] & self.__temp_rate_mambership['hot'], self.__fan_membership['fast']))

            self.__rules.append(ctrl.Rule(
                self.__temp_membership['hot'] & self.__temp_rate_mambership['cold'], self.__fan_membership['medium']))
            self.__rules.append(ctrl.Rule(
                self.__temp_membership['hot'] & self.__temp_rate_mambership['normal'], self.__fan_membership['fast']))
            self.__rules.append(ctrl.Rule(
                self.__temp_membership['hot'] & self.__temp_rate_mambership['hot'], self.__fan_membership['fast']))

            return True
        except:
            print("Error in Temperature model in apply rules process")
            return False


    def set_input_values(self , temperature , temperature_rate):
        self.temperature = self.__convert_to_fahrenheit(temperature)
        self.temperature_rate = self.__convert_to_fahrenheit(temperature_rate)
    
    def defuzzification(self):
        try:
            self.__fan_speed_ctrl = ctrl.ControlSystem(self.__rules)
            self.__fan_speed_simu = ctrl.ControlSystemSimulation(
                self.__fan_speed_ctrl)
            self.__fan_speed_simu.input['temperature'] = float(self.temperature)
            self.__fan_speed_simu.input['temperature_change_rate'] = float(self.temperature_rate)
            self.__fan_speed_simu.compute()
            return True
        except:
            print("Error in Temperature model defuzzification process")
            return False

    def get_ouput_values(self):
        """ This return dict contain fan_speed value """
    
        try:
            output = {
                "fan_speed" : self.__fan_speed_simu.output['fan_speed']
            }
            return output
        except:
            print("Error in Temperature model get output process")
            return False


# temp = TempFuzzyLogic(45, 50)

# if not temp.fuzzification():
#     print("Error on fuzzification process")
# elif not temp.apply_rules():
#     print("Error on appling rules process")
# elif not temp.defuzzification():
#     print("Error on defuzzification process")
# else:
#     print(f"Fan speed value =  {temp.get_fan_speed_value()}")
