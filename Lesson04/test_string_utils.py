import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# ==================== capitalize ====================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("тест", "Тест"),
    ("123abc", "123abc"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "   "),
    (" already Capitalized", " already capitalized"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


# ==================== trim ====================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world", "hello world"),
    ("python", "python"),
    ("  123", "123"),
    ("  04 апреля 2023", "04 апреля 2023"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("skypro   ", "skypro   "),  # пробелы в конце не удаляются
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
def test_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


# ==================== contains ====================

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "Pro", True),
    ("hello world", " ", True),
    ("12345", "3", True),
    ("тест", "е", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("SkyPro", "x", False),
    ("", "a", False),
    ("hello", "", True),  # пустой символ находится
    ("", "", True),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
def test_contains_none():
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")


# ==================== delete_symbol ====================

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello world", " ", "helloworld"),
    ("banana", "a", "bnn"),
    ("12345", "3", "1245"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("", "a", ""),
    ("hello", "", "hello"),  # пустой символ — replace ничего не меняет
    ("   ", " ", ""),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
def test_delete_symbol_none():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")
