from E9T1.knight import Knight
from E9T1.mage import Mage
from E9T1.rogue import Rogue


def attack(c1, c2):
    print("{} attacks {} ".format(c1, c2), end="")

    if not c2.is_alive():
        print("{} is beating a dead horse!".format(c1.get_name()))
        return

    life_before = c2.get_health()[0]
    c1.attack(c2)
    life_after = c2.get_health()[0]
    dmg = life_before-life_after

    print("and hits for {} damage. ".format(dmg), end="")

    if c2.is_alive():
        life = c2.get_health()
        perc = round(100 * life[0] / life[1], 1)
        print("{} still has {} ({}%) health".format(c2.get_name(), life[0], perc))
    else:
        print("{} died!".format(c2.get_name()))

k = Knight("A", 5)
m = Mage("B", 9)

attack(m, k)

print(k.get_health())
