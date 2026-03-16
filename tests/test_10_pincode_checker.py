import pytest
from src.ch10_pincode_checker import (
    check_pincode_type,
    is_valid_pincode,
    is_valid_name,
    is_valid_address,
    normalize_pincode,
)


class TestCheckPincodeType:
    def test_int_type(self):
        assert check_pincode_type(110001) == "int"

    def test_str_type(self):
        assert check_pincode_type("110001") == "str"

    def test_float_type(self):
        assert check_pincode_type(11.5) == "float"

    def test_bool_type_before_int(self):
        assert check_pincode_type(True) == "bool"
        assert check_pincode_type(False) == "bool"

    def test_list_type(self):
        assert check_pincode_type([1, 2]) == "list"

    def test_dict_type(self):
        assert check_pincode_type({"a": 1}) == "dict"

    def test_none_is_unknown(self):
        assert check_pincode_type(None) == "unknown"


class TestIsValidPincode:
    def test_valid_pincode(self):
        assert is_valid_pincode(110001) is True
        assert is_valid_pincode(999999) is True
        assert is_valid_pincode(100000) is True

    def test_out_of_range(self):
        assert is_valid_pincode(99999) is False
        assert is_valid_pincode(1000000) is False

    def test_string_pincode_invalid(self):
        assert is_valid_pincode("110001") is False

    def test_bool_pincode_invalid(self):
        assert is_valid_pincode(True) is False
        assert is_valid_pincode(False) is False

    def test_none_invalid(self):
        assert is_valid_pincode(None) is False


class TestIsValidName:
    def test_valid_name(self):
        assert is_valid_name("Ramesh") is True

    def test_empty_string_invalid(self):
        assert is_valid_name("") is False

    def test_number_invalid(self):
        assert is_valid_name(123) is False

    def test_none_invalid(self):
        assert is_valid_name(None) is False


class TestIsValidAddress:
    def test_valid_address(self):
        addr = {"street": "MG Road", "city": "Delhi", "pincode": 110001}
        assert is_valid_address(addr) is True

    def test_missing_field(self):
        assert is_valid_address({"street": "MG Road", "city": "Delhi"}) is False
        assert is_valid_address({"street": "MG Road"}) is False

    def test_non_dict_invalid(self):
        assert is_valid_address("not a dict") is False
        assert is_valid_address(None) is False


class TestNormalizePincode:
    def test_string_to_int(self):
        assert normalize_pincode("110001") == 110001

    def test_int_returns_as_is(self):
        assert normalize_pincode(110001) == 110001

    def test_invalid_string_returns_none(self):
        assert normalize_pincode("abcdef") is None
        assert normalize_pincode("110.5") is None

    def test_bool_returns_none(self):
        assert normalize_pincode(True) is None
        assert normalize_pincode(False) is None

    def test_none_returns_none(self):
        assert normalize_pincode(None) is None
