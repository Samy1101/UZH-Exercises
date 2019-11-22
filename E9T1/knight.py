# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from E9T1.character import Character


class Knight(Character):

    def _get_caused_dmg(self, other):
        damage_done = round(super()._get_caused_dmg(other) * 0.8)
        return max(1, damage_done)

    def _take_physical_damage(self, amount):
        real_amount = round(amount * 0.75)
        super()._take_physical_damage(real_amount)

