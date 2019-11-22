# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from E9T1.character import Character


class Mage(Character):

    def _get_caused_dmg(self, other):
        damage_done = round(super()._get_caused_dmg(other) * 1.25)
        return max(1, damage_done)

    def _take_physical_damage(self, amount):
        real_amount = round(amount * 1.5)
        super()._take_physical_damage(real_amount)

    def _take_magical_damage(self, amount):
        real_amount = round(amount * 1.5)
        super()._take_magical_damage(real_amount)

    def attack(self, other):
        assert isinstance(other, Character)
        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")

        other._take_magical_damage(self._get_caused_dmg(other))
