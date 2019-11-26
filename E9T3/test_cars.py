from unittest import TestCase
from E9T3.combustion_car import CombustionCar
from E9T3.electric_car import ElectricCar
from E9T3.hybrid_car import HybridCar


class TestCars(TestCase):

    def test_comb_remaining_range(self):
        c = CombustionCar(40.0, 8.0)
        self.assertAlmostEqual(500.0, c.get_remaining_range(), delta=0.001)

    def test_comb_drive(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        self.assertAlmostEqual(38.0, c.get_gas_tank_status()[0], delta=0.001)

    def test_comb_get_gas(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(100.0)
        actual = c.get_gas_tank_status()
        expected = (32.0, 40.0)
        self.assertEqual(expected, actual)

    def test_comb_fuel(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(100.0)
        c.fuel(2.0)
        actual = c.get_gas_tank_status()[0]
        expected = 34.0
        self.assertEqual(expected, actual)

    def test_comb_overfilled(self):
        c = CombustionCar(40.0, 8.0)

        with self.assertRaises(Warning):
            c.fuel(2.0)

    def test_elec_remaining_range(self):
        e = ElectricCar(40.0, 500.0)
        expected = 500.0
        actual = e.get_remaining_range()
        self.assertEqual(expected, actual)

    def test_elec_charge(self):
        e = ElectricCar(50.0, 500.0)
        e.drive(100.0)
        e.charge(2.0)
        actual = e.get_battery_status()[0]
        expected = 42.0
        self.assertEqual(expected, actual)

    def  test_elec_overcharged(self):
        e = ElectricCar(50.0, 500.0)
        with self.assertRaises(Warning):
            e.charge(2.0)

    def test_elec_get_battery(self):
        e = ElectricCar(50.0, 500.0)
        e.drive(100.0)
        actual = e.get_battery_status()
        expected = (40.0, 50.0)
        self.assertEqual(expected, actual)

    def test_hybrid_drive(self):
        h = HybridCar(16.0, 8.0, 50.0, 500.0)
        h.switch_to_combustion()
        h.drive(100.0)
        expected = 8.0
        actual = h.get_gas_tank_status()[0]
        self.assertEqual(expected, actual)

    def test_hybrid_auto_switch(self):
        h = HybridCar(16.0, 8.0, 50.0, 500.0)
        h.switch_to_combustion()
        h.drive(300.0)
        expected = 0.0
        actual = h.get_gas_tank_status()[0]
        self.assertEqual(expected, actual)

    def test_hybrid_charge(self):
        h = HybridCar(16.0, 8.0, 50.0, 500.0)
        h.switch_to_combustion()
        h.drive(400.0)
        expected = 30.0
        actual = h.get_battery_status()[0]
        self.assertEqual(expected, actual)

    def test_hybrid_range(self):
        h = HybridCar(16.0, 8.0, 50.0, 500.0)
        expected = 700.0
        actual = h.get_remaining_range()
        self.assertEqual(expected, actual)

    def test_hybrid_elec_comb_switch(self):
        h = HybridCar(16.0, 8.0, 50.0, 500.0)
        h.switch_to_electric()
        h.drive(600.0)
        expected = 8.0
        actual = h.get_gas_tank_status()[0]
        self.assertEqual(expected, actual)

    def test_hybrid_depleted(self):
        h = HybridCar(16.0, 8.0, 50.0, 500.0)

        with self.assertRaises(Warning):
            h.drive(800)

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
