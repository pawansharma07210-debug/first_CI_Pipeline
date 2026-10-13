import importlib
import pytest

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary

def test_standard_conversion():
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(255) == "11111111"

def test_zero():
    assert decimal_to_binary(0) == "0"

def test_one():
    assert decimal_to_binary(1) == "1"

def test_power_of_two():
    assert decimal_to_binary(16) == "10000"

def test_negative_raises_error():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)
