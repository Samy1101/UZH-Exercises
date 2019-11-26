# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from E9T3.combustion_car import CombustionCar
from E9T3.electric_car import ElectricCar
from E9T3.hybrid_car import HybridCar

c = CombustionCar(40.0, 8.0)
c.get_remaining_range() # 500
c.drive(500.0)
c.get_gas_tank_status() # (38.0, 40.0)
try:
    c.drive(1000.0)
except Warning:
    print("fuel is depleted")
else:
    raise Warning("Here should have been raised a warning!")


print(c.get_gas_tank_status())

e = ElectricCar(25.0, 500.0)
e.drive(200.0)
#e.charge(2.0)
print(e.get_battery_status()) # (22.0, 25)

h = HybridCar(40.0, 8.0, 25.0, 500.0)
h.switch_to_combustion()
h.drive(600.0) # depletes fuel, auto-switch
print(h.get_gas_tank_status()) # (0.0, 40.0)
print(h.get_battery_status()) # (20.0, 25.0)
