import importlib

module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort

def test_unsorted_list():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]

def test_already_sorted():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_empty_and_single_element():
    assert bubble_sort([]) == []
    assert bubble_sort([42]) == [42]

def test_negative_and_duplicates():
    assert bubble_sort([3, -1, 3, 0, -5]) == [-5, -1, 0, 3, 3]

def test_original_list_not_modified():
    original = [4, 3, 2, 1]
    sorted_copy = bubble_sort(original)
    assert original == [4, 3, 2, 1]
    assert sorted_copy == [1, 2, 3, 4]
