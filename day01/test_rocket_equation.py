from rocket_equation import fuel_calculator, fuel_requirement_sum, \
    module_with_fuel_cost


def test_mass_twelve_returns_two():
    assert fuel_calculator(12) == 2


def test_mass_fourteen_returns_two():
    assert fuel_calculator(14) == 2


def test_mass_1969_returns_654():
    assert fuel_calculator(1969) == 654


def test_mass_100756_returns_33583():
    assert fuel_calculator(100756) == 33583


def test_fuel_requirements_contains_int():
    assert isinstance(fuel_requirement_sum(), int)


def test_mass_14_with_fuel_mass_returns_2():
    assert module_with_fuel_cost(14) == 2


def test_mass_1969_with_fuel_mass_returns_966():
    assert module_with_fuel_cost(1969) == 966


def test_mass_100756_with_fuel_returns_50346():
    assert module_with_fuel_cost(100756) == 50346
