import pytest
from src.ch09_postcard_writer import (
    format_postcard_address,
    add_postcard_border,
    is_valid_greeting,
    has_proper_closing,
    format_stamp_number,
    count_words,
)


class TestFormatPostcardAddress:
    def test_basic_format(self):
        result = format_postcard_address("Sunita", "Jaipur", "302001")
        assert result == "To: Sunita\n    Jaipur - 302001"

    def test_pincode_zero_padded(self):
        result = format_postcard_address("Ritu", "Delhi", "1234")
        assert "001234" in result

    def test_non_string_returns_empty(self):
        assert format_postcard_address(123, "Jaipur", "302001") == ""
        assert format_postcard_address("Sunita", None, "302001") == ""
        assert format_postcard_address("Sunita", "Jaipur", 302001) == ""


class TestAddPostcardBorder:
    def test_centers_message(self):
        result = add_postcard_border("Namaste!", 20)
        assert result == "------Namaste!------"

    def test_non_string_message_returns_empty(self):
        assert add_postcard_border(123, 20) == ""
        assert add_postcard_border(None, 20) == ""

    def test_non_positive_width_returns_empty(self):
        assert add_postcard_border("Hi", 0) == ""
        assert add_postcard_border("Hi", -5) == ""
        assert add_postcard_border("Hi", 2.5) == ""


class TestIsValidGreeting:
    def test_namaste_prefix(self):
        assert is_valid_greeting("Namaste Sunita!") is True

    def test_dear_prefix(self):
        assert is_valid_greeting("Dear Ramesh,") is True

    def test_invalid_greeting(self):
        assert is_valid_greeting("Hey!") is False
        assert is_valid_greeting("Hello") is False

    def test_non_string_returns_false(self):
        assert is_valid_greeting(123) is False
        assert is_valid_greeting(None) is False


class TestHasProperClosing:
    def test_yours_truly_closing(self):
        assert has_proper_closing("I hope you are well. Yours truly,") is True

    def test_aapka_closing(self):
        assert has_proper_closing("Sab theek hai. Aapka,") is True

    def test_shubhkamnao_closing(self):
        assert has_proper_closing("Best wishes. Shubhkamnao,") is True

    def test_invalid_closing(self):
        assert has_proper_closing("Hello there") is False

    def test_non_string_returns_false(self):
        assert has_proper_closing(None) is False


class TestFormatStampNumber:
    def test_pads_with_zeros(self):
        assert format_stamp_number(12345) == "00012345"

    def test_exactly_8_digits(self):
        assert format_stamp_number(12345678) == "12345678"

    def test_negative_returns_empty(self):
        assert format_stamp_number(-1) == ""

    def test_non_integer_returns_empty(self):
        assert format_stamp_number("12345") == ""
        assert format_stamp_number(12.5) == ""
        assert format_stamp_number(None) == ""


class TestCountWords:
    def test_basic_word_count(self):
        assert count_words("Jai Hind Vande Mataram") == 4

    def test_single_word(self):
        assert count_words("Namaste") == 1

    def test_extra_spaces_handled(self):
        assert count_words("  Jai   Hind  ") == 2

    def test_empty_string_returns_zero(self):
        assert count_words("") == 0
        assert count_words("   ") == 0

    def test_non_string_returns_zero(self):
        assert count_words(None) == 0
        assert count_words(123) == 0
