# import numpy as np
# import skfuzzy as fuzz
# from skfuzzy import control as ctrl
from __future__ import annotations
from abc import ABCMeta, abstractmethod

# from FuzzyLogic.Interfaces import FuzzyLogicControlSystemInterface


class FuzzyLogicControlSystemInterface(metaclass=ABCMeta):
    @abstractmethod
    def __fuzzification(self):
        pass

    @abstractmethod
    def __apply_rules(self):
        pass

    @abstractmethod
    def __defuzzification(self) -> bool:
        pass


class TempFuzzyLogic(FuzzyLogicControlSystemInterface):
    def __init__(self):
        # self.__fuzzification(self)
        # self.__apply_rules(self)
        pass

    def __fuzzification(self):
        pass

    def __apply_rules(self):
        pass

    def __defuzzification(self) -> bool:
        pass

    # def __fuzzification(self):
    #     return self

    # def __apply_rules(self):
    #     return self

    # def __defuzzification(self) -> bool:
    #     pass

    def set_temperature(self, temperature) -> 'TempFuzzyLogic':
        self.temperature = temperature
        return self

    def set_temperature_rate(self, temperature_rate) -> 'TempFuzzyLogic':
        self.temperature_rate = temperature_rate
        return self

    def get_fan_speed_value(self):
        if(not self.__defuzzification()):
            return False

        pass


temp = TempFuzzyLogic()

# temp = TempFuzzyLogic(45, 50)

# temp.__fuzzification()

# if not temp.fuzzification():
#     print("Error on fuzzification process")
# elif not temp.apply_rules():
#     print("Error on appling rules process")
# elif not temp.defuzzification():
#     print("Error on defuzzification process")
# else:
#     print(f"Fan speed value =  {temp.get_fan_speed_value()}")


# class TempFuzzyLogic(FuzzyLogicControlSystemInterface):
#     def __init__(self):
#         self.__fuzzification()
#         self.__rules()

#     def __fuzzification(self):
#         self.__temp_membership = ctrl.Antecedent(
#             np.arange(0, 80, 0.1), "temperature")  # Unit is fahrenheit
#         # Rate of change of temperature = (Previous Temperature – CurrentTemperature)
#         self.__temp_rate_mambership = ctrl.Antecedent(
#             np.arange(-50, 50, 1), "temperature_change_rate")
#         self.__fan_membership = ctrl.Consequent(
#             np.arange(0, 200, 1), "fan_speed")

#         self.__temp_membership['cold'] = fuzz.trapmf(
#             self.__temp_membership.universe, [0, 0, 50, 60])
#         self.__temp_membership['normal'] = fuzz.trimf(
#             self.__temp_membership.universe, [60, 62.5, 65])
#         self.__temp_membership['hot'] = fuzz.trapmf(
#             self.__temp_membership.universe, [65, 70, 80, 80])

#         self.__temp_rate_mambership['cold'] = fuzz.trimf(
#             self.__temp_rate_mambership .universe, [-50, -10, 0])
#         self.__temp_rate_mambership['normal'] = fuzz.trimf(
#             self.__temp_rate_mambership .universe, [-10, 0, 10])
#         self.__temp_rate_mambership['hot'] = fuzz.trimf(
#             self.__temp_rate_mambership .universe, [0, 10, 50])

#         self.__fan_membership['slow'] = fuzz.trapmf(
#             self.__fan_membership.universe, [0, 0, 63, 127])
#         self.__fan_membership['medium'] = fuzz.trimf(
#             self.__fan_membership.universe, [63, 127, 191])
#         self.__fan_membership['fast'] = fuzz.trapmf(
#             self.__fan_membership.universe, [127, 191, 200, 200])

#         return True

#     def __rules(self):
#         self.__rules = []
#         self.__rules.append(ctrl.Rule(
#             self.__temp_membership['cold'] | self.__temp_rate_mambership['cold'], self.__fan_membership['slow']))
#         self.__rules.append(ctrl.Rule(
#             self.__temp_membership['cold'] | self.__temp_rate_mambership['normal'], self.__fan_membership['medium']))
#         self.__rules.append(ctrl.Rule(
#             self.__temp_membership['cold'] | self.__temp_rate_mambership['hot'], self.__fan_membership['fast']))

#         self.__rules.append(ctrl.Rule(
#             self.__temp_membership['normal'] | self.__temp_rate_mambership['cold'], self.__fan_membership['medium']))
#         self.__rules.append(ctrl.Rule(
#             self.__temp_membership['normal'] | self.__temp_rate_mambership['normal'], self.__fan_membership['medium']))
#         self.__rules.append(ctrl.Rule(
#             self.__temp_membership['normal'] | self.__temp_rate_mambership['hot'], self.__fan_membership['fast']))

#         self.__rules.append(ctrl.Rule(
#             self.__temp_membership['hot'] | self.__temp_rate_mambership['cold'], self.__fan_membership['medium']))
#         self.__rules.append(ctrl.Rule(
#             self.__temp_membership['hot'] | self.__temp_rate_mambership['normal'], self.__fan_membership['fast']))
#         self.__rules.append(ctrl.Rule(
#             self.__temp_membership['hot'] | self.__temp_rate_mambership['hot'], self.__fan_membership['fast']))

#     def set_temperature(self, temperature):
#         self.temperature = temperature

#     def set_temperature_rate(self, temperature_rate):
#         self.temperature_rate = temperature_rate

#     def __defuzzification(self):
#         try:
#             self.__fan_speed_ctrl = ctrl.ControlSystem(self.__rules)
#             self.__fan_speed_simu = ctrl.ControlSystemSimulation(
#                 self.__fan_speed_ctrl)
#             self.__fan_speed_simu.input['temperature'] = self.temperature
#             self.__fan_speed_simu.input['temperature_change_rate'] = self.temperature_rate
#             self.__fan_speed_simu.compute()

#             return True
#         except:
#             return False

#     def get_fan_speed_value(self):
#         try:
#             return self.__fan_speed_simu.output['fan_speed']
#         except:
#             return False
