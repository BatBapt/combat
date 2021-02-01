from perso import player


class Warrior(player.Player):

    def __init__(self, p_name):
        player.Player.__init__(self, p_name)
        self._att_dmg = 55
        self._armor = 20
        self._energy = 100
        self._energy_max = 100

    # Getter
    @property
    def att_dmg(self):
        return self._att_dmg

    @property
    def armor(self):
        return self._armor

    @property
    def energy(self):
        return self._energy

    @property
    def energy_max(self):
        return self._energy_max

    # Setter
    @att_dmg.setter
    def att_dmg(self, p_att_dmg):
        self._att_dmg += p_att_dmg

    @armor.setter
    def armor(self, p_armor):
        self._armor += p_armor

    @energy.setter
    def energy(self, p_energy):
        self._energy += p_energy

    @energy_max.setter
    def energy_max(self, p_energy_max):
        self._energy_max += p_energy_max

