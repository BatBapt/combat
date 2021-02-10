import json
from technic import technic

class WarriorTechContainer:
    def __init__(self, tech_file):
        brute_dict = {}
        with open(tech_file) as input_file:
            brute_dict = json.load(input_file)

        self._tech_list = []
        for name, values in brute_dict.items():
            json_to_tech = technic.Technic(name, values['description'], values['cost'])
            self._tech_list.append(json_to_tech)

    @property
    def tech_list(self):
        return self._tech_list

w = WarriorTechContainer("technic/warrior_technique.json")
