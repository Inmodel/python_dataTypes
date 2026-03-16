import pytest
import math
from src.ch03_rickshaw_meter import (
    parse_distance,
    calculate_fare,
    apply_discount,
    get_fare_range,
    get_absolute_difference,
)


class TestParseDistance:
    def test_valid_float_string(self):
        assert parse_distance("12.5") == 12.5

    def test_integer_string(self):
        assert parse_distance("10") == 10.0

    def test_invalid_string_returns_minus_one(self):
        assert parse_distance("abcd") == -1.0
        assert parse_distance("12km") == -1.0

    def test_non_string_returns_minus_one(self):
        assert parse_distance(None) == -1.0
        assert parse_distance(123) == -1.0


class TestCalculateFare:
    def test_basic_fare(self):
        assert calculate_fare(3.0, 10) == 30

    def test_rounds_up_with_ceil(self):
        assert calculate_fare(3.2, 10) == 32
        assert calculate_fare(3.5, 10) == 35

    def test_non_number_returns_minus_one(self):
        assert calculate_fare("3", 10) == -1
        assert calculate_fare(3, "10") == -1

    def test_negative_values_return_minus_one(self):
        assert calculate_fare(-3, 10) == -1
        assert calculate_fare(3, -10) == -1


class TestApplyDiscount:
    def test_basic_discount(self):
        assert apply_discount(100, 10) == 90.0

    def test_zero_discount(self):
        assert apply_discount(100, 0) == 100.0

    def test_full_discount(self):
        assert apply_discount(100, 100) == 0.0

    def test_non_number_returns_minus_one(self):
        assert apply_discount("100", 10) == -1
        assert apply_discount(100, "10") == -1

    def test_out_of_range_discount_returns_minus_one(self):
        assert apply_discount(100, -5) == -1
        assert apply_discount(100, 110) == -1


class TestGetFareRange:
    def test_basic_range(self):
        assert get_fare_range([50, 30, 80, 20]) == {"min": 20, "max": 80}

    def test_single_item(self):
        assert get_fare_range([45]) == {"min": 45, "max": 45}

    def test_non_list_returns_none(self):
        assert get_fare_range("50") is None
        assert get_fare_range(None) is None

    def test_empty_list_returns_none(self):
        assert get_fare_range([]) is None


class TestGetAbsoluteDifference:
    def test_positive_difference(self):
        assert get_absolute_difference(80, 50) == 30

    def test_reversed_order(self):
        assert get_absolute_difference(50, 80) == 30

    def test_same_values(self):
        assert get_absolute_difference(50, 50) == 0

    def test_non_number_returns_minus_one(self):
        assert get_absolute_difference("80", 50) == -1
        assert get_absolute_difference(80, None) == -1
