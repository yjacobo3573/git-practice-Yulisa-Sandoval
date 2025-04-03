import pytest
from program import divide_numbers, reverse_string, get_list_element




def test_divide_numbers_normal_case():
    assert divide_numbers(10, 2) == 5

def test_divide_numbers_zero_division_edge_case():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

def test_divide_numbers_large_number_corner_case():
    assert divide_numbers(1_000_000,0.0001) == 10000000000.0


def test_reverse_string_normal_case():
    assert reverse_string("Hello") == "OLLEh"

def test_reverse_string_empty_string_edge_case():
    assert reverse_string("") == ""

def test_reverse_string_non_string_input_corner_case():
    with pytest.raises(TypeError):
        reverse_string(12345)

def test_get_list_element_normal_case():
    assert get_list_element([1,2,3], 1) == 2

def test_get_list_element_index_out_of_range_edge_case():

     assert get_list_element([],0) == "Not found"

def test_get_list_element_non_integer_index_corner_case():
    with pytest.raises(TypeError):
        get_list_element([1,2,3], "1")
