from program_alarm import intcode_as_array


def test_array_has_ten_elements():
    intcode_list = intcode_as_array()
    assert len(intcode_list) > 9
