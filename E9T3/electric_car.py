# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from E9T3.car import Car


class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):

        self._battery_size = battery_size
        self._battery_range_km = battery_range_km
        self._current_range = battery_range_km
        self._current_charge = [battery_size, battery_size]

        if type(battery_size) != float or type(battery_range_km) != float:
            self._current_charge[0] = 0
            raise Warning("please provide float")

        if battery_size < 0 or battery_range_km < 0:
            self._current_charge[0] = 0
            raise Warning("please provide positive values")

        self._range_per_kwh = battery_range_km / battery_size
        self._kwh_per_km = battery_size / battery_range_km


    def charge(self, kwh):

        if type(kwh) != float:
            raise Warning("kwh has to be float")

        if kwh < 0:
            raise Warning("kwh has to be positive")

        self._current_charge[0] += kwh
        if self._current_charge[0] > self._battery_size:
            raise Warning("battery was overcharged")

        self._current_range += kwh * self._range_per_kwh

    def get_battery_status(self):
        return tuple(self._current_charge[:])

    def get_remaining_range(self):
        return self._current_range

    def drive(self, dist):
        if type(dist) != float:
            self._current_charge[0] = 0
            raise Warning("distance has to be float")

        if dist < 0:
            self._current_charge[0] = 0
            raise Warning("distance has to be positive")
        self._current_charge[0] -= dist * self._kwh_per_km
        self._current_range -= dist

        if self._current_charge[0] < 0:
            self._current_charge[0] = 0
            raise Warning("charge is empty")
