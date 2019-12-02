from rocket_equation import fuel_calculator


def test_mass_twelve_returns_two():
    assert fuel_calculator(12) == 2
