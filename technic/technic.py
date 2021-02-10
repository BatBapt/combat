class Technic:

    def __init__(self, p_name, p_description, p_cost):
        self._name = p_name
        self._description = p_description
        self._cost = p_cost

    # Getter
    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def cost(self):
        return self._cost

    def __repr__(self):
        return "{}: {}. Cout: {}".format(self._name, self._description, self._cost)
