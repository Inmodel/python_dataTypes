import pytest
from src.ch08_paan_shop import (
    apply_price_hike,
    filter_menu_by_price,
    merge_menus,
    get_menu_copy,
    invert_menu,
)

MENU = {"sada paan": 10, "meetha paan": 20, "banarasi paan": 50, "fire paan": 100}


class TestApplyPriceHike:
    def test_basic_hike(self):
        result = apply_price_hike({"sada": 10, "meetha": 20}, 10)
        assert result == {"sada": 11.0, "meetha": 22.0}

    def test_zero_hike(self):
        result = apply_price_hike({"sada": 10}, 0)
        assert result == {"sada": 10.0}

    def test_non_dict_returns_empty(self):
        assert apply_price_hike(None, 10) == {}
        assert apply_price_hike("not a dict", 10) == {}

    def test_non_number_percent_returns_empty(self):
        assert apply_price_hike(MENU, "10") == {}

    def test_negative_percent_returns_empty(self):
        assert apply_price_hike(MENU, -5) == {}


class TestFilterMenuByPrice:
    def test_filters_correctly(self):
        result = filter_menu_by_price(MENU, 20)
        assert result == {"sada paan": 10, "meetha paan": 20}

    def test_no_items_in_range(self):
        result = filter_menu_by_price(MENU, 5)
        assert result == {}

    def test_all_items_in_range(self):
        result = filter_menu_by_price(MENU, 1000)
        assert len(result) == 4

    def test_non_dict_returns_empty(self):
        assert filter_menu_by_price(None, 50) == {}

    def test_non_number_max_price_returns_empty(self):
        assert filter_menu_by_price(MENU, "50") == {}


class TestMergeMenus:
    def test_basic_merge(self):
        result = merge_menus({"sada": 10}, {"banarasi": 50})
        assert result == {"sada": 10, "banarasi": 50}

    def test_special_overrides_base(self):
        result = merge_menus({"sada": 10}, {"sada": 15, "banarasi": 50})
        assert result["sada"] == 15

    def test_first_not_dict_treated_as_empty(self):
        result = merge_menus(None, {"sada": 10})
        assert result == {"sada": 10}

    def test_second_not_dict_treated_as_empty(self):
        result = merge_menus({"sada": 10}, None)
        assert result == {"sada": 10}


class TestGetMenuCopy:
    def test_returns_dict(self):
        result = get_menu_copy(MENU)
        assert result == MENU

    def test_is_new_object(self):
        result = get_menu_copy(MENU)
        assert result is not MENU

    def test_non_dict_returns_empty(self):
        assert get_menu_copy(None) == {}
        assert get_menu_copy("not a dict") == {}


class TestInvertMenu:
    def test_basic_invert(self):
        result = invert_menu({"sada paan": 10, "meetha paan": 20})
        assert result == {10: "sada paan", 20: "meetha paan"}

    def test_empty_dict(self):
        assert invert_menu({}) == {}

    def test_non_dict_returns_empty(self):
        assert invert_menu(None) == {}
        assert invert_menu("not a dict") == {}
