import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class PHFuzzyLogic:
    def fuzzification(self):
        try:
            self.__ph_membership = ctrl.Antecedent(
                np.arange(0, 14, 0.001), 'ph')
            self.__water_level_membership = ctrl.Antecedent(
                np.arange(0, 40, 0.1), 'water_level')  # unit --> mm
            self.__ph_pump_membership = ctrl.Consequent(
                np.arange(0, 8, 0.1), "ph_pump")  # duration unit --> seconds
            self.__alkaline_pump_membership = ctrl.Consequent(
                np.arange(0, 8, 0.1), "alkaline_pump")  # duration unit --> seconds

            self.__ph_membership['very_low'] = fuzz.trapmf(
                self.__ph_membership.universe, [0, 0, 1.375, 2.75])
            self.__ph_membership['low'] = fuzz.trimf(
                self.__ph_membership.universe, [2, 3.75, 5.5])
            self.__ph_membership['normal'] = fuzz.trimf(
                self.__ph_membership.universe, [5.4, 6, 6.5])
            self.__ph_membership['high'] = fuzz.trimf(
                self.__ph_membership.universe, [6.4, 7.5, 9])
            self.__ph_membership['very_high'] = fuzz.trapmf(
                self.__ph_membership.universe, [8, 10, 14, 14])

            self.__water_level_membership['low'] = fuzz.trimf(
                self.__water_level_membership.universe, [0, 6.5, 13])
            self.__water_level_membership['normal'] = fuzz.trimf(
                self.__water_level_membership.universe, [12, 19.5, 26])
            self.__water_level_membership['high'] = fuzz.trimf(
                self.__water_level_membership.universe, [25, 32, 40])

            self.__ph_pump_membership["stop"] = fuzz.trimf(
                self.__ph_pump_membership.universe, [0, 0, 0])
            self.__ph_pump_membership["fast"] = fuzz.trimf(
                self.__ph_pump_membership.universe, [0, 1.5, 3.5])
            self.__ph_pump_membership["medium"] = fuzz.trimf(
                self.__ph_pump_membership.universe, [3, 4, 5.5])
            self.__ph_pump_membership["long"] = fuzz.trimf(
                self.__ph_pump_membership.universe, [5, 6.5, 8])

            self.__alkaline_pump_membership["stop"] = fuzz.trimf(
                self.__alkaline_pump_membership.universe, [0, 0, 0])
            self.__alkaline_pump_membership["fast"] = fuzz.trimf(
                self.__alkaline_pump_membership.universe, [0, 1.5, 3.5])
            self.__alkaline_pump_membership["medium"] = fuzz.trimf(
                self.__alkaline_pump_membership.universe, [3, 4, 5.5])
            self.__alkaline_pump_membership["long"] = fuzz.trimf(
                self.__alkaline_pump_membership.universe, [5, 6.5, 8])

            return True
        except:
            return False

    def apply_rules(self):
        try:
            self.__rules = []

            self.__rules.append(
                ctrl.Rule(
                    antecedent=(
                        self.__ph_membership['very_low'] & self.__water_level_membership['low']),
                    consequent=(
                        self.__ph_pump_membership['medium'], self.__alkaline_pump_membership['stop'])
                )
            )
            self.__rules.append(
                ctrl.Rule(
                    antecedent=(
                        self.__ph_membership['very_low'] & self.__water_level_membership['normal']),
                    consequent=(
                        self.__ph_pump_membership['medium'], self.__alkaline_pump_membership['stop'])
                )
            )
            self.__rules.append(
                ctrl.Rule(
                    antecedent=(
                        self.__ph_membership['very_low'] & self.__water_level_membership['high']),
                    consequent=(
                        self.__ph_pump_membership['long'], self.__alkaline_pump_membership['stop'])
                )
            )

            self.__rules.append(
                ctrl.Rule(
                    antecedent=(
                        self.__ph_membership['low'] & self.__water_level_membership['low']),
                    consequent=(
                        self.__ph_pump_membership['fast'], self.__alkaline_pump_membership['stop'])
                )
            )
            self.__rules.append(
                ctrl.Rule(
                    antecedent=(
                        self.__ph_membership['low'] & self.__water_level_membership['normal']),
                    consequent=(
                        self.__ph_pump_membership['medium'], self.__alkaline_pump_membership['stop'])
                )
            )
            self.__rules.append(
                ctrl.Rule(
                    antecedent=(
                        self.__ph_membership['low'] & self.__water_level_membership['high']),
                    consequent=(
                        self.__ph_pump_membership['medium'], self.__alkaline_pump_membership['stop'])
                )
            )

            self.__rules.append(
                ctrl.Rule(
                    antecedent=(self.__ph_membership['normal']),
                    consequent=(
                        self.__ph_pump_membership['stop'], self.__alkaline_pump_membership['stop'])
                )
            )

            self.__rules.append(
                ctrl.Rule(
                    antecedent=(
                        self.__ph_membership['high'] & self.__water_level_membership['low']),
                    consequent=(
                        self.__ph_pump_membership['stop'], self.__alkaline_pump_membership['fast'])
                )
            )
            self.__rules.append(
                ctrl.Rule(
                    antecedent=(
                        self.__ph_membership['high'] & self.__water_level_membership['normal']),
                    consequent=(
                        self.__ph_pump_membership['stop'], self.__alkaline_pump_membership['medium'])
                )
            )
            self.__rules.append(
                ctrl.Rule(
                    antecedent=(
                        self.__ph_membership['high'] & self.__water_level_membership['high']),
                    consequent=(
                        self.__ph_pump_membership['stop'], self.__alkaline_pump_membership['medium'])
                )
            )

            self.__rules.append(
                ctrl.Rule(
                    antecedent=(
                        self.__ph_membership['very_high'] & self.__water_level_membership['low']),
                    consequent=(
                        self.__ph_pump_membership['stop'], self.__alkaline_pump_membership['medium'])
                )
            )
            self.__rules.append(
                ctrl.Rule(
                    antecedent=(
                        self.__ph_membership['very_high'] & self.__water_level_membership['normal']),
                    consequent=(
                        self.__ph_pump_membership['stop'], self.__alkaline_pump_membership['medium'])
                )
            )
            self.__rules.append(
                ctrl.Rule(
                    antecedent=(
                        self.__ph_membership['very_high'] & self.__water_level_membership['high']),
                    consequent=(
                        self.__ph_pump_membership['stop'], self.__alkaline_pump_membership['long'])
                )
            )

            return True
        except:
            return False

    def set_input_values(self , ph_value , water_level_value):
        self.ph_value = ph_value
        self.water_level_value = water_level_value    
    
    def defuzzification(self):
        try:
            self.__pump_ctrl = ctrl.ControlSystem(self.__rules)
            self.__pump_sim = ctrl.ControlSystemSimulation(self.__pump_ctrl)
            self.__pump_sim.input['ph'] = self.ph_value
            self.__pump_sim.input['water_level'] = self.water_level_value
            self.__pump_sim.compute()
            return True
        except:
            return False

    def get_ouput_values(self):
        try:
            ouput = {
                "ph_pump" : self.__pump_sim.output['ph_pump'],
                "alkaline_pump": self.__pump_sim.output['alkaline_pump']
            }
            return ouput
        except:
            return False



# ph = PHFuzzyLogic(14, 40)

# if not ph.fuzzification():
#     print("Error on fuzzification process")
# elif not ph.apply_rules():
#     print("Error on appling rules process")
# elif not ph.defuzzification():
#     print("Error on defuzzification process")
# else:
#     print(f"PH pump value =  {ph.get_ph_pump_value()}")
#     print(f"PH Alkaline value =  {ph.get_alkaline_pump_value()}")
