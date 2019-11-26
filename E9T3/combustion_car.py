# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from E9T3.car import Car


class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        self._gas_capacity = gas_capacity
        self._gas_per_100km = gas_per_100km
        self._current_gas = [gas_capacity, gas_capacity]

        if type(gas_capacity) != float or type(gas_per_100km) != float:
            self._current_gas[0] = 0
            raise Warning("please provide float")

        if gas_capacity < 0 or gas_per_100km < 0:
            self._current_gas[0] = 0
            raise Warning("please provide positive values")

        self._range = gas_capacity / gas_per_100km * 100.0

    def fuel(self, f):
        if type(f) != float:
            self._current_gas[0] = 0
            raise Warning("please provide a float")

        if f < 0:
            self._current_gas[0] = 0
            raise Warning("fuel has to be positive")

        self._current_gas[0] += f

        if self._current_gas[0] > self._gas_capacity:
            self._current_gas[0] = 0
            raise Warning("car is overfilled")

    def get_gas_tank_status(self):
        return tuple(self._current_gas[:])

    def get_remaining_range(self):
        return self._range

    def drive(self, dist):
        if type(dist) != float:
            self._current_gas[0] = 0
            raise Warning("please provide a float")

        if dist < 0:
            self._current_gas[0] = 0
            raise Warning("please provide a positive distance")

        self._current_gas[0] -= self._gas_per_100km * dist/100
        if self._current_gas[0] < 0:
            self._current_gas[0] = 0
            raise Warning("the gas tank is empty")
