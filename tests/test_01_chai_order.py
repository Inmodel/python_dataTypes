import pytest
from src.ch01_chai_order import (
    get_chai_order_length,
    shout_chai_order,
    whisper_chai_order,
    has_special_ingredient,
    get_first_and_last_char,
)


class TestGetChaiOrderLength:
    def test_basic_length(self):
        assert get_chai_order_length("masala chai") == 11

    def test_trims_before_counting(self):
        assert get_chai_order_length("  masala chai  ") == 11

    def test_whitespace_only_returns_zero(self):
        assert get_chai_order_length("   ") == 0

    def test_non_string_returns_minus_one(self):
        assert get_chai_order_length(123) == -1
        assert get_chai_order_length(None) == -1
        assert get_chai_order_length([]) == -1


class TestShoutChaiOrder:
    def test_converts_to_uppercase(self):
        assert shout_chai_order("masala chai") == "MASALA CHAI"

    def test_trims_before_converting(self):
        assert shout_chai_order("  adrak chai  ") == "ADRAK CHAI"

    def test_non_string_returns_empty(self):
        assert shout_chai_order(42) == ""
        assert shout_chai_order(None) == ""

    def test_empty_string_returns_empty(self):
        assert shout_chai_order("") == ""
        assert shout_chai_order("   ") == ""


class TestWhisperChaiOrder:
    def test_converts_to_lowercase(self):
        assert whisper_chai_order("ADRAK CHAI") == "adrak chai"

    def test_trims_before_converting(self):
        assert whisper_chai_order("  ELAICHI CHAI  ") == "elaichi chai"

    def test_non_string_returns_empty(self):
        assert whisper_chai_order(100) == ""
        assert whisper_chai_order(None) == ""

    def test_empty_or_whitespace_returns_empty(self):
        assert whisper_chai_order("") == ""
        assert whisper_chai_order("  ") == ""


class TestHasSpecialIngredient:
    def test_finds_ingredient_case_insensitive(self):
        assert has_special_ingredient("Elaichi Masala Chai", "elaichi") is True

    def test_finds_ingredient_when_order_is_lowercase(self):
        assert has_special_ingredient("adrak wali chai", "ADRAK") is True

    def test_returns_false_when_not_found(self):
        assert has_special_ingredient("masala chai", "elaichi") is False

    def test_returns_false_for_non_string_inputs(self):
        assert has_special_ingredient(123, "chai") is False
        assert has_special_ingredient("chai", 123) is False
        assert has_special_ingredient(None, None) is False


class TestGetFirstAndLastChar:
    def test_returns_first_and_last(self):
        assert get_first_and_last_char("masala chai") == {"first": "m", "last": "i"}

    def test_trims_before_getting_chars(self):
        assert get_first_and_last_char("  adrak  ") == {"first": "a", "last": "k"}

    def test_single_character(self):
        assert get_first_and_last_char("a") == {"first": "a", "last": "a"}

    def test_returns_none_for_non_string(self):
        assert get_first_and_last_char(42) is None
        assert get_first_and_last_char(None) is None

    def test_returns_none_for_empty_or_whitespace(self):
        assert get_first_and_last_char("") is None
        assert get_first_and_last_char("   ") is None
