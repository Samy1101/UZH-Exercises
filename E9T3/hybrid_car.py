# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from E9T3.combustion_car import CombustionCar
from E9T3.electric_car import ElectricCar


class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self._mode = None               # True = Combustion-mode
        self._remaining_charge = battery_size

    def switch_to_combustion(self):
        self._mode = True

    def switch_to_electric(self):
        self._mode = False

    def get_remaining_range(self):
        return CombustionCar.get_remaining_range(self) + ElectricCar.get_remaining_range(self)

    def drive(self, dist):

        if type(dist) != float:
            self._current_gas[0] = 0
            self._current_charge[0] = 0
            raise Warning("distance has to be float")

        if dist < 0:
            self._current_gas[0] = 0
            self._current_charge[0] = 0
            raise Warning("distance has to be positive")

        remaining_gas = self._current_gas[0] - self._gas_per_100km * dist/100
        remaining_charge = self._current_charge[0] - dist * self._kwh_per_km

        if self._mode:
            if remaining_gas < 0:
                self._current_gas[0] = 0
                remaining_range = abs(remaining_gas / self._gas_per_100km * 100)
                ElectricCar.drive(self, remaining_range)

            else:
                CombustionCar.drive(self, dist)

        if not self._mode:
            if remaining_charge < 0:
                self._current_charge[0] = 0
                remaining_range = abs(self._battery_range_km - dist)
                CombustionCar.drive(self, remaining_range)

            else:
                ElectricCar.drive(self, dist)

        if self._current_gas[0] <= 0 and self._current_charge[0] <= 0:
            self._current_gas[0] = 0
            self._current_charge[0] = 0
            raise Warning("both the battery and the gas tank have been depleted")
