import pytest
from program import divide_numbers, reverse_string, get_list_element

def test_divide_numbers_normal_case():
    assert divide_numbers(10, 2) == 5.0

def test_divide_numbers_zero_division_edge_case():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

def test_divide_numbers_large_number_corner_case():
    assert divide_numbers(1_000_000,0.0001) == 10000000000.0