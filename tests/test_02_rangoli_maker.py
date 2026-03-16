import pytest
from src.ch02_rangoli_maker import (
    repeat_pattern,
    extract_rangoli_center,
    split_and_join_rangoli,
    replace_rangoli_color,
    make_rangoli_border,
)


class TestRepeatPattern:
    def test_basic_repeat(self):
        assert repeat_pattern("*-", 4) == "*-*-*-*-"

    def test_single_repeat(self):
        assert repeat_pattern("*", 5) == "*****"

    def test_non_string_returns_empty(self):
        assert repeat_pattern(123, 3) == ""
        assert repeat_pattern(None, 3) == ""

    def test_non_positive_times_returns_empty(self):
        assert repeat_pattern("*", 0) == ""
        assert repeat_pattern("*", -1) == ""
        assert repeat_pattern("*", 2.5) == ""


class TestExtractRangoliCenter:
    def test_basic_slice(self):
        assert extract_rangoli_center("***LOTUS***", 3, 8) == "LOTUS"

    def test_empty_slice(self):
        assert extract_rangoli_center("HELLO", 2, 2) == ""

    def test_non_string_design_returns_empty(self):
        assert extract_rangoli_center(123, 0, 3) == ""
        assert extract_rangoli_center(None, 0, 3) == ""

    def test_non_integer_indices_returns_empty(self):
        assert extract_rangoli_center("HELLO", "a", 3) == ""
        assert extract_rangoli_center("HELLO", 0, "b") == ""


class TestSplitAndJoinRangoli:
    def test_basic_split_join(self):
        assert split_and_join_rangoli("red,blue,green", ",", " | ") == "red | blue | green"

    def test_changes_separator(self):
        assert split_and_join_rangoli("red-blue", "-", ",") == "red,blue"

    def test_non_string_returns_empty(self):
        assert split_and_join_rangoli(123, ",", "-") == ""
        assert split_and_join_rangoli(None, ",", "-") == ""


class TestReplaceRangoliColor:
    def test_replaces_all_occurrences(self):
        assert replace_rangoli_color("red-blue-red-green-red", "red", "pink") == "pink-blue-pink-green-pink"

    def test_no_change_if_not_found(self):
        assert replace_rangoli_color("blue-green", "red", "pink") == "blue-green"

    def test_non_string_returns_empty(self):
        assert replace_rangoli_color(123, "red", "pink") == ""
        assert replace_rangoli_color("red", 123, "pink") == ""
        assert replace_rangoli_color("red", "red", 123) == ""


class TestMakeRangoliBorder:
    def test_single_char_border(self):
        assert make_rangoli_border("*", 5) == "*****"

    def test_two_char_pattern_border(self):
        assert make_rangoli_border("=-", 7) == "=-=-=-="

    def test_non_string_returns_empty(self):
        assert make_rangoli_border(123, 5) == ""
        assert make_rangoli_border(None, 5) == ""

    def test_non_positive_length_returns_empty(self):
        assert make_rangoli_border("*", 0) == ""
        assert make_rangoli_border("*", -3) == ""
