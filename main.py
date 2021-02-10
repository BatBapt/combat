from perso.warrior import Warrior


w = Warrior("Baptiste", 55, 20)
w1 = Warrior("Paul", 20, 10)

w1.heal()

w.attack(w1)

print(w)
