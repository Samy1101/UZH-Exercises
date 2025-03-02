# This is the class that you have found online. Do not edit this file
# and implement your extension through inheritance only. Any change
# in this file will be reset for the grading!


class Character:

    def __init__(self, name, lvl):
        assert isinstance(name, str)
        assert isinstance(lvl, int)
        assert lvl > 0
        assert name
        self._name = name
        self._lvl = lvl
        self._health_max = lvl * 50
        self._health_cur = self._health_max

    def get_name(self):
        return self._name

    def get_lvl(self):
        return self._lvl

    def get_health(self):
        return (self._health_cur, self._health_max)

    def attack(self, other):
        assert isinstance(other, Character)
        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")

        other._take_physical_damage(self._get_caused_dmg(other))

    def _get_caused_dmg(self, other):
        return max(1, self._lvl * 11 - other._lvl)

    def _take_physical_damage(self, amount):
        assert isinstance(amount, int)
        assert amount >= 0
        self._health_cur = max(0, self._health_cur - amount)

    def _take_magical_damage(self, amount):
        assert isinstance(amount, int)
        assert amount >= 0
        self._health_cur = max(0, self._health_cur - amount)

    def is_alive(self):
        return self._health_cur > 0

    def __repr__(self):
        s = "{} ({}, {}, {}/{})"
        return s.format(self._name, type(self).__name__, self._lvl, self._health_cur, self._health_max)
