from perso import player


class Warrior(player.Player):

    def __init__(self, p_name, p_att_dmg, p_armor):
        player.Player.__init__(self, p_name, p_att_dmg, p_armor)
        self._energy = 100
        self._energy_max = 100

    # Getters
    @property
    def energy(self):
        return self._energy

    @property
    def energy_max(self):
        return self._energy_max

    # Setters
    @energy.setter
    def energy(self, p_energy):
        self._energy += p_energy

    @energy_max.setter
    def energy_max(self, p_energy_max):
        self._energy_max += p_energy_max

    # Methods
    def __repr__(self):
        string = player.Player.__repr__(self)
        string += " Je suis un Guerrier."
        return string
