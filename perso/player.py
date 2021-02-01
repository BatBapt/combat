from perso import perso

from random import randint


class Player(perso.Perso):

    def __init__(self, p_name):
        perso.Perso.__init__(self, p_name)
        self._hp = 100
        self._hp_max = 100
        self._exp = 0
        self._gold = 50
        self._level = 1
        self._alive = True

    # Getter
    @property
    def hp(self) -> float:
        return self._hp

    @property
    def hp_max(self) -> float:
        return self._hp_max

    @property
    def exp(self) -> int:
        return self._exp

    @property
    def gold(self) -> int:
        return self._gold

    @property
    def level(self):
        return self._level

    @property
    def alive(self) -> bool:
        return self._alive

    # Setter
    @hp.setter
    def hp(self, p_hp):
        self._hp += p_hp

    @hp_max.setter
    def hp_max(self, p_hp_max):
        self._hp += p_hp_max

    @gold.setter
    def gold(self, p_gold):
        self._gold += p_gold

    @alive.setter
    def alive(self, p_alive):
        self._alive = p_alive

    # Methods
    def __repr__(self):
        msg = "Je suis le joueur {}, j'ai {} PV sur {}. J'ai {} expérience et je suis niveau {}. Je possède {} or".\
            format(self._name, self._hp, self._hp_max, self._exp, self._level, self._gold)
        return msg

    def level_up(self):
        self._level += 1

    def receive_dmg(self, dammage) -> bool:
        self._hp = -dammage
        if self._hp <= 0:
            print("{} est mort...".format(self._name))
            self.alive = False
            return False
        else:
            print("{} a perdu {} PV. Il lui en reste {}".format(self._name, dammage, self.hp))
            return True

    def heal(self) -> bool:
        if self._hp <= self._hp_max:
            health_profit = randint(15, 30)
            self._hp = health_profit
            if self._hp > self._hp_max:
                self._hp = self._hp_max
            print("Vous êtes guérris de {} PV".format(health_profit))
            return True
        else:
            print("Vous avez déjà vos PV max")
            return False
