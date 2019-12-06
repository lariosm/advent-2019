from secure_container import is_six_digits, contains_adjacent_digits,\
    digit_increase_check, password_criteria, possible_password_combinations,\
    contains_matching_adjacent_digits


def test_six_digit_function_works():
    assert is_six_digits(251903)
    assert not is_six_digits(3256)


def test_contains_adjacent_works():
    assert contains_adjacent_digits(122545)
    assert not contains_adjacent_digits(412390)


def test_digits_never_decrease():
    assert digit_increase_check(122567)
    assert not digit_increase_check(225434)


def test_value_meets_password_criteria():
    assert password_criteria(223344)


def test_possible_password_combo_returns_length():
    assert isinstance(possible_password_combinations(), int)


def test_contains_special_adjacent_digits_is_true():
    assert contains_matching_adjacent_digits(112233)


def test_contains_special_adjacent_digits_is_false():
    assert not contains_matching_adjacent_digits(123444)
