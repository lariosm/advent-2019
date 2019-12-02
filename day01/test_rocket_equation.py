from rocket_equation import fuel_calculator


def test_mass_twelve_returns_two():
    assert fuel_calculator(12) == 2


def test_mass_fourteen_returns_two():
    assert fuel_calculator(14) == 2


def test_mass_1969_returns_654():
    assert fuel_calculator(1969) == 654
