import pytest
from src.ch04_sabzi_mandi import (
    add_to_cart,
    add_urgent_item,
    remove_last_item,
    is_in_cart,
    merge_carts,
)


class TestAddToCart:
    def test_adds_item_and_returns_length(self):
        assert add_to_cart(["tamatar", "pyaaz"], "mirchi") == 3

    def test_empty_cart(self):
        assert add_to_cart([], "tamatar") == 1

    def test_non_list_cart_returns_minus_one(self):
        assert add_to_cart("not a list", "item") == -1
        assert add_to_cart(None, "item") == -1

    def test_empty_string_item_no_addition(self):
        cart = ["tamatar"]
        result = add_to_cart(cart, "")
        assert result == 1

    def test_non_string_item_no_addition(self):
        cart = ["tamatar"]
        result = add_to_cart(cart, 123)
        assert result == 1


class TestAddUrgentItem:
    def test_adds_to_beginning(self):
        assert add_urgent_item(["pyaaz", "mirchi"], "dhaniya") == ["dhaniya", "pyaaz", "mirchi"]

    def test_empty_cart(self):
        assert add_urgent_item([], "tamatar") == ["tamatar"]

    def test_non_list_returns_empty(self):
        assert add_urgent_item("not a list", "item") == []
        assert add_urgent_item(None, "item") == []

    def test_invalid_item_returns_cart_unchanged(self):
        cart = ["tamatar"]
        result = add_urgent_item(cart, "")
        assert result == ["tamatar"]


class TestRemoveLastItem:
    def test_removes_last(self):
        assert remove_last_item(["tamatar", "pyaaz", "mirchi"]) == "mirchi"

    def test_single_item_cart(self):
        assert remove_last_item(["tamatar"]) == "tamatar"

    def test_empty_cart_returns_none(self):
        assert remove_last_item([]) is None

    def test_non_list_returns_none(self):
        assert remove_last_item("not a list") is None
        assert remove_last_item(None) is None


class TestIsInCart:
    def test_item_present(self):
        assert is_in_cart(["tamatar", "pyaaz"], "pyaaz") is True

    def test_item_absent(self):
        assert is_in_cart(["tamatar", "pyaaz"], "mirchi") is False

    def test_non_list_returns_false(self):
        assert is_in_cart("not a list", "item") is False
        assert is_in_cart(None, "item") is False


class TestMergeCarts:
    def test_basic_merge(self):
        assert merge_carts(["tamatar"], ["mirchi", "adrak"]) == ["tamatar", "mirchi", "adrak"]

    def test_first_not_list_treated_as_empty(self):
        assert merge_carts(None, ["mirchi"]) == ["mirchi"]

    def test_second_not_list_treated_as_empty(self):
        assert merge_carts(["tamatar"], None) == ["tamatar"]

    def test_both_empty(self):
        assert merge_carts([], []) == []
