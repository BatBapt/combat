from perso import player
from technic import warrior_tech_container


class Warrior(player.Player):

    def __init__(self, p_name, p_att_dmg, p_armor):
        player.Player.__init__(self, p_name, p_att_dmg, p_armor)
        self._energy = 100
        self._energy_max = 100

        self._warrior_technique = warrior_tech_container.WarriorTechContainer("technic/warrior_technique.json").tech_list


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

    def learn_special_attack(self):
        player.Player.learn_special_attack(self)
        for i, tech in enumerate(self._warrior_technique):
            print("[{}]: {}".format(i, tech))

        which_tech_learn = int(input("Que voulez vous apprendre comme technique? "))
        if which_tech_learn < 0 or which_tech_learn >= len(self._warrior_technique):
            print("Erreur")
