from secure_container import is_six_digits


def test_six_digit_function_works():
    assert is_six_digits(251903)
    assert not is_six_digits(3256)
