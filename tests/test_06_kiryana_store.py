import pytest
from src.ch06_kiryana_store import (
    get_item_totals,
    get_expensive_items,
    calculate_total_bill,
    sort_by_price,
    apply_tax,
)

ITEMS = [
    {"name": "atta", "price": 50, "qty": 2, "category": "grocery"},
    {"name": "daal", "price": 120, "qty": 1, "category": "grocery"},
    {"name": "oil", "price": 200, "qty": 1, "category": "grocery"},
    {"name": "namak", "price": 20, "qty": 3, "category": "spice"},
]


class TestGetItemTotals:
    def test_basic_totals(self):
        result = get_item_totals([{"name": "atta", "price": 50, "qty": 2}])
        assert result == [{"name": "atta", "total": 100}]

    def test_multiple_items(self):
        result = get_item_totals(ITEMS)
        assert len(result) == 4
        assert result[0] == {"name": "atta", "total": 100}
        assert result[1] == {"name": "daal", "total": 120}

    def test_non_list_returns_empty(self):
        assert get_item_totals(None) == []
        assert get_item_totals("not a list") == []


class TestGetExpensiveItems:
    def test_filters_by_threshold(self):
        result = get_expensive_items(ITEMS, 100)
        names = [i["name"] for i in result]
        assert "daal" in names
        assert "oil" in names
        assert "atta" not in names
        assert "namak" not in names

    def test_no_items_above_threshold(self):
        assert get_expensive_items(ITEMS, 500) == []

    def test_non_list_returns_empty(self):
        assert get_expensive_items(None, 100) == []

    def test_non_number_threshold_returns_empty(self):
        assert get_expensive_items(ITEMS, "100") == []


class TestCalculateTotalBill:
    def test_basic_total(self):
        items = [{"price": 50, "qty": 2}, {"price": 30, "qty": 3}]
        assert calculate_total_bill(items) == 190.0

    def test_single_item(self):
        assert calculate_total_bill([{"price": 100, "qty": 1}]) == 100.0

    def test_empty_list_returns_zero(self):
        assert calculate_total_bill([]) == 0.0

    def test_non_list_returns_zero(self):
        assert calculate_total_bill(None) == 0.0


class TestSortByPrice:
    def test_ascending_sort(self):
        result = sort_by_price(ITEMS)
        prices = [i["price"] for i in result]
        assert prices == sorted(prices)

    def test_descending_sort(self):
        result = sort_by_price(ITEMS, ascending=False)
        prices = [i["price"] for i in result]
        assert prices == sorted(prices, reverse=True)

    def test_non_list_returns_empty(self):
        assert sort_by_price(None) == []


class TestApplyTax:
    def test_basic_tax(self):
        result = apply_tax([{"name": "atta", "price": 50, "qty": 2}], 10)
        assert result == [{"name": "atta", "total_with_tax": 110.0}]

    def test_zero_tax(self):
        result = apply_tax([{"name": "atta", "price": 50, "qty": 2}], 0)
        assert result == [{"name": "atta", "total_with_tax": 100.0}]

    def test_non_list_returns_empty(self):
        assert apply_tax(None, 10) == []

    def test_non_number_tax_returns_empty(self):
        assert apply_tax(ITEMS, "10") == []
