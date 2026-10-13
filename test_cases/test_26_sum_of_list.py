import importlib

module = importlib.import_module("26_sum_of_list")
sum_of_list = module.sum_of_list

def test_standard_sum():
    assert sum_of_list([1, 2, 3, 4]) == 10

def test_empty_list():
    assert sum_of_list([]) == 0

def test_single_element():
    assert sum_of_list([25]) == 25

def test_negative_and_zero():
    assert sum_of_list([-5, 5, -10, 10, 0]) == 0
