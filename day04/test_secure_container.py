from secure_container import is_six_digits, contains_adjacent_digits


def test_six_digit_function_works():
    assert is_six_digits(251903)
    assert not is_six_digits(3256)


def test_contains_adjacent_works():
    assert contains_adjacent_digits(122545)
    assert not contains_adjacent_digits(412390)
