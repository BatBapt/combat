from perso import perso

from random import randint


class Player(perso.Perso):

    def __init__(self, p_name, p_att_dmg, p_armor):
        perso.Perso.__init__(self, p_name)
        self._hp = 100
        self._hp_max = 100
        self._exp = 0
        self._gold = 50
        self._level = 1
        self._alive = True
        self._att_dmg = p_att_dmg
        self._armor = p_armor
        self._learnt_tech = []

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

    @property
    def att_dmg(self):
        return self._att_dmg

    @property
    def armor(self):
        return self._armor

    # Setter
    @hp.setter
    def hp(self, p_hp):
        self._hp += p_hp
        if self._hp <= 0:
            self._alive = False
        elif self._hp > self._hp_max:
            self._hp = self._hp_max

    @hp_max.setter
    def hp_max(self, p_hp_max):
        self._hp += p_hp_max

    @exp.setter
    def exp(self, p_exp):
        self._exp += p_exp

    @gold.setter
    def gold(self, p_gold):
        self._gold += p_gold

    @alive.setter
    def alive(self, p_alive):
        self._alive = p_alive

    @att_dmg.setter
    def att_dmg(self, p_att_dmg):
        self._att_dmg += p_att_dmg

    @armor.setter
    def armor(self, p_armor):
        self._armor += p_armor

    # Methods
    def __repr__(self) -> str:
        msg = "Je suis le joueur {}, j'ai {} PV sur {}. J'ai {} expérience et je suis niveau {}. Je possède {} or.".\
            format(self._name, self._hp, self._hp_max, self._exp, self._level, self._gold)
        return msg

    def level_up(self) -> None:
        self._exp += randint(15, 30)
        if self._exp >= 100:
            self._exp = 0
            self._level += 1
            self._gold = randint(20, 50)
            self._att_dmg += randint(10, 20)
            self._armor += randint(5, 10)
            print("*" * 55)
            print("{} gagne un niveau ! Il est désormais niveau {}".format(self._name, self._level))
            print("*" * 55)

    def attack(self, enemy) -> bool:
        if self._att_dmg <= enemy.armor:
            print("Votre attaque est inutile")
            return enemy.alive
        else:
            print("{} attaque {}".format(self.name, enemy.name))
            still_alive = enemy.receive_dmg(enemy, self._att_dmg - enemy.armor)
            if not still_alive:
                self.level_up()
                return enemy.alive

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

    def learn_special_attack(self):
        if self._level > 1 and self._level % 2 == 0:
            print("Bravo ! Vous pouvez apprendre une nouvelle technique parmis celle-ci :")
        else:
            return 
