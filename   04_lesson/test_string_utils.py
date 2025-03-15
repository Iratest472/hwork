import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.parametrize("string, symbol", [("SkyPro", "S"), ("SkyPro", "U"), ("SkyPro", "t")])
def test_contains_positive(string, symbol):
    assert string_utils.contains( "SkyPro", "S") == True
    assert string_utils.contains("Skypro", "U") == False
    return symbol in string

@pytest.mark.parametrize("string,symbol", [("SkyPro", "k"), ("SkyPro", "Pro")])
def test_delete_symbol_positive(string, symbol):
    string = "SkyPro"
    symbol = symbol
    result = string.replace(symbol, "")

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("[]", "[]")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("123", "123")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected