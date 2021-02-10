class Perso:

    def __init__(self, p_name):
        self._name = p_name

    @property
    def name(self):
        return self._name

    # Methods
    def receive_dmg(self, ennemy, dammage) -> bool:
        ennemy.hp = -dammage
        if not ennemy.alive:
            print("{} est mort.".format(ennemy.name))
            return False
        else:
            print("{} a perdu {} PV. Il lui en reste {}.".format(ennemy.name, dammage, ennemy.hp))
